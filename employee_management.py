class Employee:
    all_employees = []
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.retired = False
        Employee.all_employees.append(self)

    @classmethod
    def get_eligible_retirees(cls):
        can_retire = [e for e in list(filter(lambda p: p.age > 66, cls.all_employees))]
        return [e for e in can_retire]

    @classmethod
    def retire_all_eligible(cls):
        can_retire = cls.get_eligible_retirees()
        [e.retire() for e in can_retire]
        return [f"{e.name} has now retired." for e in can_retire]

    @classmethod
    def all(cls):
        return cls.all_employees


    def retire(self):
        self.retired = True
        Employee.all_employees.remove(self)
        return f"{self.name} has retired"

e1 = Employee("John", 67)
e2 = Employee("Alice", 40)
e3 = Employee("Barbara", 77)

print([f"{e.name} may retire." for e in Employee.get_eligible_retirees()])
# ['John may retire.', 'Barbara may retire.']

print(Employee.retire_all_eligible())
# ['John has now retired.', 'Barbara has now retired.']

print(e1.retired)
# True

print(e2.retired)
# False

print(e3.retired)
# True