class Employee:

    def __init__(self,employeeNo,employeeName,employeeSalary,employeeDeptno):
        self.Empno = employeeNo
        self.Ename = employeeName
        self.Salary = employeeSalary
        self.Deptno = employeeDeptno
        

    def showEmployee(self):
        print("Employee # : {} \nEmployee Name : {}\nSalary :{}\nDepartment # : {}".format(self.Empno, 
        self.Ename, self.Salary,self.Deptno))   

class Salesman(Employee):
    def __init__(self,employeeNo,employeeName,employeeSalary,employeeDeptno,comm):
        self.commission = comm
        super().__init__(employeeNo,employeeName,employeeSalary,employeeDeptno)

    def showEmployee(self):
        super().showEmployee()
        print("Cpmmission :",emp.commission)


emp = Salesman(101,"shaker",5400, 10, 500)
emp.showEmployee()
