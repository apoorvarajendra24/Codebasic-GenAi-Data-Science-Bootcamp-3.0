import mysql.connector
from decorator import contextmanager
from logging_setup import setup_logger

logger = setup_logger('db_helper')

@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'root',
        database = 'expense_manager'
    )
    if connection.is_connected():
        print("Connection Successful")
    else:
        print("Failed in connecting to database")
    
    cursor = connection.cursor(dictionary=True)

    yield cursor
    
    if commit:
        connection.commit()  

    cursor.close()
    connection.close()

def fetch_all_records():
    logger.info(f'fetch_all_records from the database')
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses")
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)

def fetch_expenses_for_date(expense_date):
    logger.info(f'fetch_expenses_for_date called with {expense_date}')
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s" , (expense_date,))
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)
        return expenses

def insert_expense(expense_date, amount, category, notes):
    logger.info(f'insert_expense_for_date called with: {expense_date}, amount: {amount}, category: {category}, notes: {notes}')
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
                       (expense_date, amount, category, notes))

def delete_expense_for_date(expense_date):
    logger.info(f'delete_expense_for_date called with {expense_date}')
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))

def fetch_expense_summary(start_date, end_date):
    logger.info(f'fetch_expense_summary with start: {start_date}, end: {end_date}')
    with get_db_cursor() as cursor:
        cursor.execute(
        """SELECT category , SUM(amount) as total 
        FROM expenses 
        WHERE expense_date 
        BETWEEN %s and %s
        GROUP BY category
        """,(start_date, end_date) 
        )
        data = cursor.fetchall()
        return data
if __name__ == "__main__":
    # print("----------expense for 08/04------------")
    # #insert_expense('2024-08-04','30000','sip','investment')
    # #fetch_all_records()
    # fetch_expenses_for_date("2024-08-04")
    # print("----------delete expense for 08/04-------------")
    # delete_expense_for_date('2024-08-04')
    # print("--------------expense for 08/04------------")
    # fetch_expenses_for_date("2024-08-04")

    summary = fetch_expense_summary('2024-08-01', '2024-08-04')
    for data in summary:
        print(data['category'], data['total'])