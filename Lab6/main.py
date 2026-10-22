class Worker:
    def __init__(self, working_hours, hourly_rate, bonus_coefficient):
        self.working_hours = working_hours
        self.hourly_rate = hourly_rate
        self.bonus_coefficient = bonus_coefficient

    def calculate_salary(self):
        return self.working_hours * self.hourly_rate

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Можно складывать сотрудников только одного класса")
        return self.calculate_salary() + other.calculate_salary()

    def calculate_bonus(self):
        return self.calculate_salary() * self.bonus_coefficient

    def salary_to_hours_ratio(self):
        if self.working_hours == 0:
            raise ValueError("Рабочее время не может быть равно нулю")
        return self.calculate_salary() / self.working_hours


class SeniorWorker(Worker):
    pass


class Director(SeniorWorker):
    pass


a = Worker(40, 15, 0.1)
b = Worker(35, 20, 0.15)

print(a.calculate_salary())  # Output: 600
print(a.calculate_salary() + a.calculate_bonus()) # Output: 660
print()
print(b.calculate_salary())  # Output: 700
print(b.calculate_salary() + b.calculate_bonus())# Output: 805
print(a + b)  # Output: 1300