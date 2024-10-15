from typing import Any


class Vacancy:
    __slots__ = ["title", "link", "salary", "description"]

    def __init__(self, title, link, salary, description):
        self.title = title
        self.link = link
        self.salary = self.parse_salary(salary)  # Преобразуем зарплату к числовому виду
        self.description = description

    def validate_salary(self, salary):
        # Здесь может быть любая логика, проверяющая формат зарплаты
        return salary if salary else "Зарплата не указана"

    def parse_salary(self, salary):
        # Предполагаем, что зарплата может быть строкой или числом
        if isinstance(salary, str):
            # Пример: зарплата может быть в формате "100 000-150 000 руб."
            salary_range = salary.split("-")
            try:
                # Преобразуем первую часть зарплатного диапазона в число
                return int(salary_range[0].replace(" ", "").replace("руб.", "").strip())
            except (ValueError, IndexError):
                return 0  # Если не удается преобразовать, вернем 0
        elif isinstance(salary, (int, float)):
            return salary
        else:
            return 0

    def __lt__(self, other: Any) -> bool:
        return self.salary < other.salary

    def __str__(self):
        return f"{self.title}: {self.salary}\n{self.link}\n{self.description}\n"
