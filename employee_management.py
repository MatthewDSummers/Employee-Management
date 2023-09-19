class Employee:
    all_employees = {}

    def __init__(self, name, age):
        self.id = Employee.generate_object_id()
        self.name = name
        self.age = age
        self.retired = False
        Employee.all_employees[self.id] = self

    @classmethod
    def generate_object_id(cls):
        if not hasattr(cls, "object_id"):
            cls.object_id = 0
        cls.object_id += 1
        return cls.object_id

    @classmethod
    def all(cls, status=None):
        if status:
            if status == "Retired":
                return {e_id: e for e_id, e in cls.all_employees.items() if e.retired}
            elif status == "Active":
                return {e_id: e for e_id, e in cls.all_employees.items() if not e.retired}
        return cls.all_employees

    @classmethod
    def get_eligible_retirees(cls, ignore=None):
        if ignore is None:
            ignore = []
        not_ignored = {e_id: e for e_id, e in cls.all_employees.items() if e_id not in ignore}
        return {e_id: e for e_id, e in not_ignored.items() if e.age > 66 and not e.retired}

    @classmethod
    def retire_eligible(cls, ignore=[]):
        can_retire = cls.get_eligible_retirees(ignore=ignore)
        return [m.retire() for m in can_retire.values()]

    def retire(self):
        if not self.retired:
            self.retired = True
            return f"{self.name} has now retired"

e1 = Employee("John", 67)
e2 = Employee("Alice", 40)
e3 = Employee("Barbara", 77)
e4 = Employee("David", 80)

print(e1.retired)
# False

print(e2.retired)
# False

print(e3.retired)
# False

print(e4.retired)
# False

candidates = Employee.get_eligible_retirees()
print([f"{e.name} may retire." for e in candidates.values()])
# ['John may retire.', 'Barbara may retire.', 'David may retire.']

print(Employee.retire_eligible(ignore=[3]))
# ['John has now retired', 'David has now retired']

print(Employee.retire_eligible())
# ['Barbara has now retired']

print(e1.retired)
# True

print(e2.retired)
# False

print(e3.retired)
# True

print(e4.retired)
# True

print(Employee.all())
# returns dict of all Employee objects

retirees = Employee.all(status="Retired")
print([f"{e.name} is a retiree." for e in retirees.values()])
# returns dict of all retired employees
# prints ['John is a retiree.', 'Barbara is a retiree.', 'David is a retiree.']

still_employed = Employee.all(status="Active")
print([f"{e.name} is currently employed." for e in still_employed.values()])
# returns dict of all current employees
# prints ['Alice is currently employed.']