from backend.supabase_client import supabase

from datetime import date


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