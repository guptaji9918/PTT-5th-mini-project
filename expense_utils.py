import math
import random
from datetime import datetime


def validate_expense(description, category, amount, expense_date):
    if not description.strip():
        raise ValueError("Description cannot be empty.")
    if not category.strip():
        raise ValueError("Category cannot be empty.")
    try:
        amount = float(amount)
    except (TypeError, ValueError):
        raise ValueError("Amount must be a number.")
    if not math.isfinite(amount) or amount <= 0:
        raise ValueError("Amount must be a positive number.")

    if isinstance(expense_date, str):
        try:
            expense_date = datetime.strptime(expense_date, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Date must use YYYY-MM-DD format.")
    return {
        "description": description.strip(),
        "category": category.strip().title(),
        "amount": round(amount, 2),
        "date": expense_date,
    }


def generate_reference_id(existing_ids=None):
    existing_ids = existing_ids or set()
    while True:
        reference_id = f"EXP-{random.randint(100000, 999999)}"
        if reference_id not in existing_ids:
            return reference_id


def calculate_total(expenses):
    return round(sum(expense["amount"] for expense in expenses), 2)


def summarize_categories(expenses):
    totals = {}
    for expense in expenses:
        category = expense["category"]
        totals[category] = totals.get(category, 0) + expense["amount"]
    return {category: round(amount, 2) for category, amount in totals.items()}