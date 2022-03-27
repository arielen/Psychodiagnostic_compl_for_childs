class Test:

    def __init__(self) -> None:
        self.instruction = "Тест. "
        self.genders = ("Мужской", "Женский")
        self.tests = (
            "1. Опросник К.Леонгарда – Г. Шмишека для исследования акцентуированных свойств личности",
            "2. Шкала личностной тревожности для учащихся 10-16 лет",
            "3. Цветовой тест отношений (ЦТО) А. М. Эткинда",
            "4. МЕТОДИКА «ЦВЕТОВОЙ ТЕСТ ОТНОШЕНИЙ» (ЦТО). ДЕТСКИЙ ВАРИАНТ ДИАГНОСТИКИ ОТНОШЕНИЯ К НРАВСТВЕННЫМ НОРМАМ",
            "5. ТЕСТ КЕТТЕЛЛА, ДЕТСКИЙ ВАРИАНТ. АДАПТИРОВАН Э. М. АЛЕКСАНДРОВСКОЙ. 12 ФЛО-120",
            "6. ШКАЛА СОЦИАЛЬНОЙ ПОДДЕРЖКИ (МНОГОМЕРНАЯ ШКАЛА ВОСПРИЯТИЯ СОЦИАЛЬНОЙ ПОДДЕРЖКИ – MSPSS ; Д.ЗИМЕТ; АДАПТАЦИЯ В. М. ЯЛТОНСКИЙ, Н. А. СИРОТА)"
        )

    def parse_result(self) -> list:
        return

    def get_instruction(self) -> str:
        return self.instruction

    def get_tests(self) -> list:
        return self.tests

    def get_genders(self) -> list:
        return self.genders


def main() -> None:

    t = Test()
    print(t.instruction)
    # t.instruction("asd")
    # print(t.instruction)


if __name__ == "__main__":
    main()
