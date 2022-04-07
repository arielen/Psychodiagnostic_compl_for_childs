import json
from tests.leonhard_schmishek import Leonhard_Schmishek


class Test:

    def __init__(self) -> None:
        self.instruction = "Тест. "
        self.genders = ("Мужской", "Женский")
        with open("tests/tests_data.json", "r", encoding="utf-8") as f:
            self.data = json.load(f)
        self.tests = {
            0: {"name": "1. Опросник К.Леонгарда – Г. Шмишека для исследования акцентуированных свойств личности",
                "instruction": self.data["Леонгарда-Шмишека"]["instruction"]},
            1: {"name": "2. Шкала личностной тревожности для учащихся 10-16 лет",
                "instruction": self.data["Шкала личностной тревожности для учащихся 10-16 лет"]["instruction"]},
            2: {"name": "3. Цветовой тест отношений (ЦТО) А. М. Эткинда",
                "instruction": self.data["Цветовой тест отношений Эткинда"]["instruction"]},
            3: {"name": "4. МЕТОДИКА «ЦВЕТОВОЙ ТЕСТ ОТНОШЕНИЙ» (ЦТО). ДЕТСКИЙ ВАРИАНТ ДИАГНОСТИКИ ОТНОШЕНИЯ К НРАВСТВЕННЫМ НОРМАМ",
                "instruction": self.data["Цветовой тест отношений Эткинда детский вариант"]["instruction"]},
            4: {"name": "5. ТЕСТ КЕТТЕЛЛА, ДЕТСКИЙ ВАРИАНТ. АДАПТИРОВАН Э. М. АЛЕКСАНДРОВСКОЙ. 12 ФЛО-120",
                "instruction": self.data["Тест Кеттелла"]["instruction"]},
            5: {"name": "6. ШКАЛА СОЦИАЛЬНОЙ ПОДДЕРЖКИ (МНОГОМЕРНАЯ ШКАЛА ВОСПРИЯТИЯ СОЦИАЛЬНОЙ ПОДДЕРЖКИ – MSPSS ; Д.ЗИМЕТ; АДАПТАЦИЯ В. М. ЯЛТОНСКИЙ, Н. А. СИРОТА)",
                "instruction": self.data["Шкала социальной поддержки"]["instruction"]}
        }

    def parse_result(self) -> list:
        return

    def get_instruction(self, cur_test: int) -> str:
        """Возвращает str данные о тесте и его инструкции 
        """
        return f"{self.instruction} {self.tests[cur_test]['name']}\n{self.tests[cur_test]['instruction']}"

    def get_tests(self) -> tuple:
        """Возвращает генератор всех тестов 
        """
        return (self.tests[test]["name"] for test in self.tests)

    def get_genders(self) -> tuple:
        """Возвращает генератор всех полов
        """
        return self.genders


def main() -> None:

    t = Test()
    print(t.instruction)
    # t.instruction("asd")
    # print(t.instruction)


if __name__ == "__main__":
    main()
