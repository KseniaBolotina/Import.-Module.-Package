from application.salary import *
from application.db.people import *
import datetime

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(f'Текущее время - {datetime.datetime.today()}')