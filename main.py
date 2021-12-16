from datetime import date, datetime
from package.application.salary import calculate_salary
from package.db.people import get_employees


if __name__ == '__main__':
    
    current_date = datetime.now()
    get_employees()
    calculate_salary()
    print(current_date)
    
    

