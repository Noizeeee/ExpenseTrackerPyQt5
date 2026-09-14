from backend.expense_manager import get_all_expenses

try:
    expenses = get_all_expenses()
    print(expenses)

except Exception as e:
    print("ERROR:")
    print(e)