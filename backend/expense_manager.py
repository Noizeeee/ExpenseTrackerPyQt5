from backend.supabase_client import supabase

from datetime import date

#Bar Graph
def get_monthly_expenses():
    response = (
        supabase
        .table("expenses")
        .select("date, amount")
        .execute()
    )

    expenses = response.data

    monthly_expenses = [0] * 12

    for expense in expenses:
        date = expense["date"]
        amount = float(expense["amount"])

        month = int(date[5:7])
        monthly_expenses[month - 1] += amount

    return monthly_expenses

#Pie Chart
def get_current_month_category_expenses():

    today = date.today()
    start_date = today.replace(day=1)

    if today.month == 12:
        next_month = date(today.year + 1, 1, 1)
    else:
        next_month = date(today.year, today.month + 1, 1)

    response = (
        supabase
        .table("expenses")
        .select("category, amount, date")
        .gte("date", start_date.isoformat())
        .lt("date", next_month.isoformat())
        .execute()
    )

    category_totals = {}

    for expense in response.data:
        category = expense["category"]
        amount = float(expense["amount"])

        if category not in category_totals:
            category_totals[category] = 0

        category_totals[category] += amount

    return category_totals

def get_all_expenses():
    response = (
        supabase
        .table("expenses")
        .select("date, description, category, amount")
        .order("date", desc=True)
        .execute()
    )

    return response.data


#Cards backend
def cards_function():
    total_expenses = 0
    try:
        expenses = get_all_expenses()
    except Exception as e:
        print(f"Error: {e}")

    for expense in expenses:
        current_expense = expense["amount"]
        total_expenses += float(current_expense)

    return f"₱ {total_expenses}"

#Current Month
def get_current_month_expenses():
    today = date.today()

    start_of_month = today.replace(day=1)

    if today.month == 12:
        start_of_next_month = today.replace(
            year=today.year + 1,
            month=1,
            day=1
        )
    else:
        start_of_next_month = today.replace(
            month=today.month + 1,
            day=1
        )
    try:
        response = (
            supabase
            .table("expenses")
            .select("*")
            .gte("date", str(start_of_month))
            .lt("date", str(start_of_next_month))
            .execute()
        )
    except Exception as e:
        print(f"Error: {e}")

    total = 0
    for expense in response.data:
        currentAmount = expense["amount"]
        total += float(currentAmount)
    
    return f"₱ {total}"

#Average Daily
def get_average_daily():
    total = 0
    try:
        amount = get_all_expenses()
        record = len(amount)
    except Exception as e:
        print(f"Error: {e}")

    for expense in amount:
        current = expense["amount"]
        total += float(current)

    average = total / record
    return f"₱ {average:.2f}"
