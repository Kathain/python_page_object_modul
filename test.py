class Employee:
    def __init__(self, name, position, hours_worked, hourly_rate):
        self.name = name
        self.__position = position
        self.__hours_worked = hours_worked
        self.__hourly_rate = hourly_rate

    def __calculate_salary(self):
        res = self.__hours_worked * self.__hourly_rate
        return res

    def _set_position(self, new_position):
        self.__position = new_position

    def get_position(self):
        return self.__position

    def get_salary(self):
        return self.__calculate_salary()

    def get_employee_details(self):
        salary = self.__calculate_salary()
        return f"Name: {self.name}, Position: {self.__position}, Salary: {salary}"


print('Good')

if __name__ == '__main__':
    employee = Employee("Джеки Чан", 'manager', 20, 40)
    print(employee.get_employee_details())  # 'Name: Джеки Чан, Position: manager, Salary: 800'
