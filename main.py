import datetime as dt
import expense_utils as eu
from report_utils import get_current_month, get_monthly_expenses, build_monthly_report


def main():
    expenses = []
    print("Personal Expense Tracker")

    while True:
        description = input("Enter description (or 'done' to finish): ").strip()
        if description.lower() == "done":
            break

        category = input("Enter category (food, travel, study, bills, other): ").strip()
        amount = input("Enter amount: ").strip()
        date_text = input("Enter date (YYYY-MM-DD, blank for today): ").strip()

        if not date_text:
            expense_date = dt.date.today()
        else:
            expense_date = date_text

        try:
            expense = eu.validate_expense(description, category, amount, expense_date)
            existing_ids = {item["reference_id"] for item in expenses}
            expense["reference_id"] = eu.generate_reference_id(existing_ids)
            expenses.append(expense)
            print(f"Expense recorded. Reference ID: {expense['reference_id']}\n")
        except ValueError as error:
            print(f"Invalid expense: {error}\n")

    year, month = get_current_month()
    monthly_expenses = get_monthly_expenses(expenses, year, month)
    total = eu.calculate_total(monthly_expenses)
    category_totals = eu.summarize_categories(monthly_expenses)
    report = build_monthly_report(
        monthly_expenses, year, month, total, category_totals
    )
    print()
    print(report)


if __name__ == "_main_":
    main()