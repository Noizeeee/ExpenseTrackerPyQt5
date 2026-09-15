from backend.supabase_client import supabase


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