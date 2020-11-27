class Employee:
    TotalEmployees = 0

    def __init__(self, employeeNo, employeeName, employeeSalary, employeeDeptno):
        self.Empno = employeeNo
        self.Ename = employeeName
        self.Salary = employeeSalary
        self.Deptno = employeeDeptno
        Employee.TotalEmployees += 1

    def showEmployee(self):
        print("Employee # : {} \nEmployee Name : {}\nSalary :{}\nDepartment # : {}".format(self.Empno,
                                                                                           self.Ename, self.Salary,
                                                                                           self.Deptno))


emp1 = Employee(101, "Shekar", 4500, 10)
emp2 = Employee(102, "Srinivassan", 5000, 20)

print("Total Employees :", Employee.TotalEmployees)
emp1.showEmployee()
emp2.showEmployee()
