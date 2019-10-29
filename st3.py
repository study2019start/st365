class Employee:
   '所有员工的基类'
   empCount = 0
 
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      #Employee.empCount += 1
      
      
   def intt(self,ss):
      
      self.e1=Employee(self.name, self.salary)
      self.e1.name=self.name+ss
      Employee.empCount=Employee.empCount+1
      return self.e1

   def displayCount(self):
        print("Total Employee %d" % Employee.empCount)
 
   def displayEmployee(self):
        print("Name : ", self.name,  ", Salary: ", self.salary)
 
"创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)
"创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)
print(Employee.empCount)
print(emp1.intt("1").intt("22").intt("333").name)
print(Employee.empCount)