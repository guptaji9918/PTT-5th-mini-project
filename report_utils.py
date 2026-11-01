import datetime as dt
import os
from tabulate import tabulate


def get_current_month():
    today = dt.date.today()
    return today.year, today.month


def get_monthly_expenses(expenses, year=None, month=None):
    if year is None or month is None:
        year, month = get_current_month()
    return [
        expense for expense in expenses
        if expense["date"].year == year and expense["date"].month == month
    ]


def build_monthly_report(expenses, year, month, total, category_totals):
    month_name = dt.date(year, month, 1).strftime("%B %Y")
    rows = [
        [
            expense["reference_id"],
            expense["date"].isoformat(),
            expense["description"],
            expense["category"],
            f"{expense['amount']:.2f}",
        ]
        for expense in expenses
    ]
    table = tabulate(
        rows,
        headers=["Reference ID", "Date", "Description", "Category", "Amount"],
        tablefmt="grid",
    )
    lines = [
        "----- MONTHLY EXPENSE REPORT -----",
        f"Report month: {month_name}",
        table if rows else "No expenses recorded for this month.",
        f"Total spending: {total:.2f}",
        "Category totals:",
    ]
    if category_totals:
        for category, amount in sorted(category_totals.items()):
            lines.append(f"  {category}: {amount:.2f}")
    else:
        lines.append("  No category totals.")
    return "\n".join(lines)


def get_report_path(filename="monthly_report.txt"):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)


def report_file_exists(path):
    return os.path.exists(path)