""" There are Employees. An Employee has a name and salary (monthly). As Employee objects are created, you need to keep a track of the total salary
    that the company has to pay on a monthly basis and it should be returned when you invoke Employee.getTotalSalary() function.
    Employee can work. An emp must be given a Job to work. A Job has a description and effort as attributes.
    Accept Job as a parameter in work() and ensure that no other data typed args are accepted. How can you validate this?
"""

class Employee():

    emp_count = 0 #class variable to check number of employee objects created
    emp_dic = {} # class variable of type dictionary to hold details of employees and salary

    def __init__(self,ename:"str",salary:"int")->"None":
        """ dunder method to create instance variables """
        Employee.emp_count += 1
        self.name = ename
        self.salary = salary
        Employee.emp_dict(self.name,self.salary)

    def work(self,job:"class")->"None":
        """ instance method to show the job description for requested employee"""
        job = Job()
        job.description = "bonda soup preparer"
        job.efforts = "1 hour effort"
        print("{} job description is {} and need {}".format(self.name,job.description,job.efforts))

    @classmethod
    def emp_dict(cls,cnt:"str",emp_name:"str")->"None":
        """ class function to add the employee salary information to emp_dic dictionary"""
        cls.emp_dic[cnt] = emp_name

    @classmethod
    def getTotalSalary(cls)->"int":
        """ class function to return the total salary to be paid depending on no of employees """
        return sum(cls.emp_dic.values())

class Job():
    '''Job class which has description and efforts attributes'''
    pass


e1 = Employee("bala",1000)
print(e1.emp_count)
e2 = Employee('smi',2000)
print(e1.emp_count)
print(Employee.emp_dic)
print(Employee.getTotalSalary())
e1.work(Job)