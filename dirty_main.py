from datetime import date, datetime
from package.application.salary import *
from package.db.people import *




if __name__ == '__main__':
    current_date = datetime.now()
    get_employees()
    calculate_salary()
    print(current_date)
    