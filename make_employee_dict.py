# Author: Ashton Lee
# Github User: ashton01L
# Date: 8/8/2024
# Description: Define a class named Employee that has private data members for an
# employee's '_name', '_ID_number', '_salary', and '_email_address'.
class Employee:
    """
    A class to represent an employee with a name, ID number, salary, and email address.

    Attributes:
    _name (str):  The employee's name
    _ID_number (str):  The employee's unique ID number
    _salary (float):  The employee's salary
    _email_address (str):  The employee's email address
    """

    def __init__(self, name, ID_number, salary, email_address):
        """
        Initializes an Employee object with the provided name, ID number, salary, and email address.

        :param name:  Employee name
               ID_number:  Employee ID number
               salary:  Employee salary
               email_address:  Employee email address
        """
        self._name = name
        self._ID_number = ID_number
        self._salary = salary
        self._email_address = email_address

    def get_name(self):
        """Returns the name of the employee."""
        return self._name

    def get_ID_number(self):
        """Returns the ID number of the employee."""
        return self._ID_number

    def get_salary(self):
        """Returns the salary of the employee."""
        return self._salary

    def get_email_address(self):
        """Returns the email address of the employee."""
        return self._email_address


def make_employee_dict(names, ids, salaries, emails):
    """
    Creates a dictionary of Employee objects from lists of names, ID numbers, salaries, and email addresses and uses
    the ID_number as key.

    :param names:  (list of str): A list of employee names.
           ids:  (list of str): A list of employee ID numbers.
           salaries:  (list of float): A list of employee salaries.
           emails: (list of str): A list of employee email addresses.

    :return: dict: A dictionary where the keys are employee ID numbers and the values are Employee objects.
    """

    employee_dict = {}

    for i in range(len(names)):
        # Create an Employee object
        employee = Employee(names[i], ids[i], salaries[i], emails[i])

        # Add the Employee object to the dictionary with ID number as the key
        employee_dict[ids[i]] = employee

    return employee_dict

names = ["Peter Parker", "Miles Morales", "Gwen Stacy", "Harry Osborn"]
ids = ["E616", "E90214", "E688B", "E1048"]
salaries = [70000, 33000, 82000, 100000]
emails = ["peter.parker@thedailybugle.com", "miles.morales@thedailybugle.com", "gwen.stacy@oscorp.com", "harry.osborn@oscorp.com"]

employee_dict = make_employee_dict(names, ids, salaries, emails)

# Example of accessing an employee's data using their ID number
# for emp_id, employee in employee_dict.items():
#     print(f"ID: {emp_id}")
#     print(f"Name: {employee.get_name()}")
#     print(f"Salary: {employee.get_salary()}")
#     print(f"Email: {employee.get_email_address()}")
#     print()
