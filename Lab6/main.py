class Worker:
    def __init__(self, working_hours:int, hourly_rate:int, bonus_coefficient:int):
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

    def __repr__(self):
        name = self.__class__.__name__
        attrs = ', '.join(f'{key} = {value}' for key, value in self.__dict__.items())
        return f'{name}({attrs})'


class SeniorWorker(Worker):
    def calculate_bonus(self):
        base_bonus = super().calculate_bonus()
        return base_bonus + 200
        

class Director(SeniorWorker):
    def change_hourly_rate(self, worker:Worker, new_rate:int):
        if not isinstance(worker, Worker):
            raise TypeError("Изменять ставку можно только объектам класса Worker или его наследников")
        elif isinstance(worker, Director):
            raise TypeError("Директор не может менять ставку другим директорам (или самому себе)")
        elif new_rate < 0:
            raise TypeError("Почасовая ставка должна быть неотрицательна")

        print(f'{self.__class__.__name__} изменил {worker.__class__.__name__} ставку с {worker.hourly_rate} на {new_rate}')
        worker.hourly_rate = new_rate



if __name__ == "__main__":
    a = Worker(40, 15, 0.1)
    b = SeniorWorker(35, 20, 0.15)
    c = Director(30, 30, 0.2)

    print(a.calculate_salary())  # Output: 600
    print(a.calculate_salary() + a.calculate_bonus()) # Output: 660
    print()
    print(b.calculate_salary())  # Output: 700
    print(b.calculate_salary() + b.calculate_bonus())# Output: 1005
    print(a + a)  # Output: 1200
    print()
    print(b)
    c.change_hourly_rate(b,100)
    print(b)
    try:
        c.change_hourly_rate(c,100000)
    except Exception as e:
        print(e)