import json
from tests.leonhard_schmishek import Leonhard_Schmishek
from tests.scale_of_personal_anxiety import ScaleOfPersonalAnxiety


class Test:

    def __init__(self) -> None:
        self.instruction = "Тест. "
        self.genders = ("Мужской", "Женский")
        with open("tests/tests_data.json", "r", encoding="utf-8") as f:
            self.data = json.load(f)
        self.tests = {
            0: {"name": "1. Опросник К.Леонгарда – Г. Шмишека для исследования акцентуированных свойств личности",
                "instruction": self.data["Леонгарда-Шмишека"]["instruction"],
                "questions": self.data["Леонгарда-Шмишека"]["questions"],
                "object": Leonhard_Schmishek},
            1: {"name": "2. Шкала личностной тревожности для учащихся 10-16 лет",
                "instruction": self.data["Шкала личностной тревожности для учащихся 10-16 лет"]["instruction"],
                "questions": self.data["Шкала личностной тревожности для учащихся 10-16 лет"]["formA"]["questions"],
                "object": ScaleOfPersonalAnxiety},
            2: {"name": "3. Цветовой тест отношений (ЦТО) А. М. Эткинда",
                "instruction": self.data["Цветовой тест отношений Эткинда"]["instruction"],
                "questions": self.data["Цветовой тест отношений Эткинда"]["questions"],
                "object": 'pass'},
            3: {"name": "4. МЕТОДИКА «ЦВЕТОВОЙ ТЕСТ ОТНОШЕНИЙ» (ЦТО). ДЕТСКИЙ ВАРИАНТ ДИАГНОСТИКИ ОТНОШЕНИЯ К НРАВСТВЕННЫМ НОРМАМ",
                "instruction": self.data["Цветовой тест отношений Эткинда детский вариант"]["instruction"],
                "object": "pass"},
            4: {"name": "5. ТЕСТ КЕТТЕЛЛА, ДЕТСКИЙ ВАРИАНТ. АДАПТИРОВАН Э. М. АЛЕКСАНДРОВСКОЙ. 12 ФЛО-120",
                "instruction": self.data["Тест Кеттелла"]["instruction"],
                "object": 'pass'},
            5: {"name": "6. ШКАЛА СОЦИАЛЬНОЙ ПОДДЕРЖКИ (МНОГОМЕРНАЯ ШКАЛА ВОСПРИЯТИЯ СОЦИАЛЬНОЙ ПОДДЕРЖКИ – MSPSS ; Д.ЗИМЕТ; АДАПТАЦИЯ В. М. ЯЛТОНСКИЙ, Н. А. СИРОТА)",
                "instruction": self.data["Шкала социальной поддержки"]["instruction"],
                "object": 'pass'},
        }
        self.cur_test = None

    def parse_result(self) -> list:
        return

    def get_instruction(self, cur_test: int) -> str:
        """Возвращает str данные о тесте и его инструкции 
        """
        return f"{self.instruction} {self.tests[cur_test]['name']}\n{self.tests[cur_test]['instruction']}"

    def get_tests(self) -> tuple:
        """Возвращает генератор с названиями всех тестов 
        """
        return (self.tests[test]["name"] for test in self.tests)

    def get_genders(self) -> tuple:
        """Возвращает генератор с названиями всех полов
        """
        return self.genders

    def get_questions(self, index: int) -> list:
        """Возвращает список вопросов на определенный тест
        """
        return self.tests[index]['questions']

    def get_cur_question(self) -> str:
        pass

    def set_data(self, last_name: str, name: str, surname: str, gender: str, age: int) -> None:
        """Задать фамилию, имя, отчество, пол, возраст для прохождения теста 
        """
        self.last_name = last_name
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age

    def init_test(self, cur_test: int) -> None:
        cur_test = self.tests[cur_test]['object']
        if cur_test is Leonhard_Schmishek:
            self.cur_test = Leonhard_Schmishek()
        elif cur_test is ScaleOfPersonalAnxiety:
            self.cur_test = ScaleOfPersonalAnxiety(
                age=self.age, gender=self.gender)


def main() -> None:
    t = Test()


if __name__ == "__main__":
    main()
