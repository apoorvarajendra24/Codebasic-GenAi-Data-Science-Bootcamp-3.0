from backend import db_helper

def test_fetch_expense_for_data():
    expenses = db_helper.fetch_expenses_for_date('2024-08-01')

    assert len(expenses) == 5
    assert expenses[0]['amount'] == 1227
    assert expenses[0]['category'] == "Rent"
    assert expenses[0]['notes'] == "Monthly rent payment"


def test_fetch_expense_for_invalid_date():
    expenses = db_helper.fetch_expenses_for_date('9999-08-01')

    assert len(expenses) == 0

def test_fetch_expense_summary_invalid_range():
    summary = db_helper.fetch_expense_summary('2055-08-09','2056-08-09')

    assert len(summary) == 0

