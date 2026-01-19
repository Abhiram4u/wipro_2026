class MarksDescriptor:
    def __set__(self, instance, value):
        if any(m < 0 or m > 100 for m in value):
            raise ValueError("Marks should be between 0 and 100")
        instance.__dict__['marks'] = value

    def __get__(self, instance, owner):
        return instance.__dict__['marks']


class SalaryDescriptor:
    def __get__(self, instance, owner):
        raise PermissionError("Access Denied: Salary is confidential")

    def __set__(self, instance, value):
        instance.__dict__['_salary'] = value
