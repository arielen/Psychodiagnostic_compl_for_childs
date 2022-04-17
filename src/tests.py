import json


class Test:

    def __init__(self, lastname: str = "", name: str = "", surname: str = "", age: int = 0, gender: str = "Мужской") -> None:
        self.lastname, self.name, self.surname = lastname, name, surname
        self.age, self.gender = age, gender
        self.genders = ("Мужской", "Женский")
        self.cur_quest_ind = 0
        self.data = None
        self.question = "Вопрос"
        self.choices = []
        self.tests = {
            0: {"name": "1. Опросник К.Леонгарда – Г. Шмишека для исследования акцентуированных свойств личности"},
            1: {"name": "2. Шкала личностной тревожности для учащихся 10-16 лет"},
            2: {"name": "3. Цветовой тест отношений (ЦТО) А. М. Эткинда"},
            3: {"name": "4. МЕТОДИКА «ЦВЕТОВОЙ ТЕСТ ОТНОШЕНИЙ» (ЦТО). ДЕТСКИЙ ВАРИАНТ ДИАГНОСТИКИ ОТНОШЕНИЯ К НРАВСТВЕННЫМ НОРМАМ"},
            4: {"name": "5. ТЕСТ КЕТТЕЛЛА, ДЕТСКИЙ ВАРИАНТ. АДАПТИРОВАН Э. М. АЛЕКСАНДРОВСКОЙ. 12 ФЛО-120"},
            5: {"name": "6. ШКАЛА СОЦИАЛЬНОЙ ПОДДЕРЖКИ (МНОГОМЕРНАЯ ШКАЛА ВОСПРИЯТИЯ СОЦИАЛЬНОЙ ПОДДЕРЖКИ – MSPSS ; Д.ЗИМЕТ; АДАПТАЦИЯ В. М. ЯЛТОНСКИЙ, Н. А. СИРОТА)"},
        }

    def get_data(self) -> dict:
        return self.data

    def get_genders(self) -> tuple:
        return self.genders

    def get_tests(self) -> tuple:
        """ Возвращает генератор с названиями всех тестов 
        """
        return (self.tests[test]["name"] for test in self.tests)

    def get_instruction(self) -> str:
        return self.data["instruction"]

    def get_question(self) -> str:
        return self.question

    def get_quest_ind(self) -> int:
        return self.cur_quest_ind

    def get_result(self) -> dict:
        """ Возвращает результаты выполнения тестов.
        По умолчанию: Данные о тестируемом 
        """
        return {"lastname": self.lastname, "name": self.name, "surname": self.surname, "age": self.age, "gender": self.gender}

    def get_questions_len(self) -> int:
        """ Возвращает количество всех тестов
        """
        return len(self.data["questions"])

    def added_choice(self, question: int) -> None:
        """ Принимает номер вопроса и добавляет его в список ответов
        """
        self.choices.append(question+1)

    def create_data(self, test: str) -> dict:
        """ Создание dict для удобного представления данных о тесте
        Принимает название теста, возвращает все данные хранящиеся 
        об этом тесте в json
        """
        with open("src/tests_data.json", 'r', encoding="utf-8") as f:
            return json.load(f)[test]

    def next_quest(self) -> None:
        """ Увеличивает индекс текущего вопроса и переопределяет вопрос
        """
        self.cur_quest_ind += 1
        self.question = self.data["questions"][self.cur_quest_ind]


class Leonhard(Test):
    """ Опросник К.Леонгарда – Г.Шмишека 
    для исследования акцентуированных свойств личности
    Шкалы:
        Гипертммность, Застревание, Эмотивность, Педантичность, 
        Тревожность, Циклотимность, Демонстративность, Возбудимость, 
        Возбудимость, Экзальтированность
    Если по какой-либо из черт испытуемый набирает более 12 баллов, 
    то данная черта считается акцентуированной. 
    Результат в 24 балла — требует дополнительного обследования, 
    например, по методике УНП или др.
    """

    def __init__(self, lastname: str = "", name: str = "", surname: str = "", age: int = 0, gender: str = "Мужской") -> None:
        super().__init__(lastname, name, surname, age, gender)

        self.data = self.create_data(test="Леонгарда-Шмишека")
        self.rating = self.data['rating']
        self.question = self.data["questions"][self.cur_quest_ind]
        self.hyperthymia = self.lateness = 0
        self.emotivity = self.pedantry = 0
        self.anxiety = self.cyclothymicity = 0
        self.demonstrativeness = self.excitability = 0
        self.distimism = self.exaltation = 0

    def get_result(self) -> dict:
        """ Возвращает словарь с результатами, где ключ = Характеристике,
        а значение кол-ву очков. 
        """
        result = super().get_result()
        result.update({"Гипертимность": self.hyperthymia, "Застревание": self.hyperthymia,
                       "Эмотивность": self.emotivity, "Педантичность": self.pedantry,
                       "Тревожность": self.anxiety, "Циклотимность": self.cyclothymicity,
                       "Демонстративность": self.demonstrativeness, "Возбудимость": self.excitability,
                       "Дистимичность": self.distimism, "Экзальтированность": self.exaltation})
        # проверяем результаты
        for key, data in self.rating.items():
            for answer in data['answers']:
                if (answer > 0 and answer in self.choices) or (answer < 0 and answer not in self.choices):
                    result[key] += data['multiply']
        self.check_accentuated(result)
        return result

    def check_accentuated(self, result: dict) -> None:
        """ Проверка акцентируемых черт 
        """
        features = (
            "Гипертимность", "Застревание", "Эмотивность", "Педантичность",
            "Тревожность", "Циклотимность", "Демонстративность",
            "Возбудимость", "Дистимичность", "Экзальтированность")
        for feature in features:
            if result[feature] >= 24:
                result[feature] = "Требует дополнительного обследования"
            elif result[feature] > 12:
                result[feature] = "Акцентируемая черта"
            else:
                result[feature] = "В пределах нормы"


class ScaleOfPersonalAnxiety(Test):
    """ Шкала личностной тревожности для учащихся 10-16 лет
    Описание методики:
        Методика относится к числу бланковых, что позволяет проводить ее коллективно. 
    Бланк содержит необходимые сведения об испытуемом, инструкцию и содержание методики:
        Методика разработана в двух формах;
        Форма А предназначена для школьников 10-12 лет;
        Форма Б — для учащихся 13-16 лет;
        Инструкция к обеим формам одинакова.
    Шкалы:
        Школьная тревожность;
        Самооценочная тревожность;
        Межличностная тревожность;
        Магическая тревожность.
    """

    def __init__(self, lastname: str = "", name: str = "", surname: str = "", age: int = 0, gender: str = "Мужской") -> None:
        super().__init__(lastname, name, surname, age, gender)
        self.data = self.create_data(
            test="Шкала личностной тревожности для учащихся 10-16 лет")
        self.rating = self.data['rating']
        self.question = self.data["formA"]["questions"][self.cur_quest_ind]

    def next_quest(self) -> None:
        self.cur_quest_ind += 1
        self.question = self.data["formA"]["questions"][self.cur_quest_ind]

    def get_questions_len(self) -> int:
        pass


class ColorRelationship(Test):
    """ Цветовой тест отношений (ЦТО) А.М.Эткинда

    """

    def __init__(self, lastname: str = "", name: str = "", surname: str = "", age: int = 0, gender: str = "Мужской") -> None:
        super().__init__(lastname, name, surname, age, gender)
        self.data = self.create_data(test="Цветовой тест отношений Эткинда")
        self.question = self.data["questions"][self.cur_quest_ind]


class ColorRelationshipKid(ColorRelationship):
    """ МЕТОДИКА «ЦВЕТОВОЙ ТЕСТ ОТНОШЕНИЙ» (ЦТО). 
    ДЕТСКИЙ ВАРИАНТ ДИАГНОСТИКИ ОТНОШЕНИЯ К НРАВСТВЕННЫМ НОРМАМ.
    НАЗНАЧЕНИЕ ТЕСТА:
        Методика предназначена для изучения эмоционального отношения ребенка к нравственным
    Шкалы: 
        отношение к нравственным нормам
    """

    def __init__(self, lastname: str = "", name: str = "", surname: str = "", age: int = 0, gender: str = "Мужской") -> None:
        super().__init__(lastname, name, surname, age, gender)
        self.data = self.create_data(
            test="Цветовой тест отношений Эткинда детский вариант")
        self.question = self.data["questions"][self.cur_quest_ind]


class Cattell(Test):
    """ ТЕСТ КЕТТЕЛЛА, ДЕТСКИЙ ВАРИАНТ. АДАПТИРОВАН Э.М.АЛЕКСАНДРОВСКОЙ. 12 ФЛО-120
    НАЗНАЧЕНИЕ ТЕСТА:
        Оценка индивидуально-психологических особенностей личности.
    Шкалы:
        общительность, вербальный интеллект, уверенность в себе, 
        возбудимость, склонность к самоутверждению, 
        склонность к риску, ответственность, социальная смелость, 
        чувствительность, тревожность, самоконтроль, нервное напряжение

    """

    def __init__(self, lastname: str = "", name: str = "", surname: str = "", age: int = 0, gender: str = "Мужской") -> None:
        super().__init__(lastname, name, surname, age, gender)
        self.data = self.create_data(test="Тест Кеттелла")
        self.question = self.data["formBoysP1"]["questions"][self.cur_quest_ind] if self.gender == "Мужской" else self.data["formGirlsP1"]["questions"][self.cur_quest_ind]

    def next_quest(self) -> None:
        self.cur_quest_ind += 1
        self.question = self.data["formBoysP1"]["questions"][self.cur_quest_ind] if self.gender == "Мужской" else self.data["formGirlsP1"]["questions"][self.cur_quest_ind]

    def get_questions_len(self) -> int:
        return len(self.data["formBoysP1"]["questions"]) if self.gender == "Мужской" else len(self.data["formGirlsP1"]["questions"][self.cur_quest_ind])


class SocialSupportScale(Test):
    """ ШКАЛА СОЦИАЛЬНОЙ ПОДДЕРЖКИ 
    (МНОГОМЕРНАЯ ШКАЛА ВОСПРИЯТИЯ СОЦИАЛЬНОЙ ПОДДЕРЖКИ – MSPSS; Д.ЗИМЕТ; АДАПТАЦИЯ В.М.ЯЛТОНСКИЙ, Н.А.СИРОТА)
    НАЗНАЧЕНИЕ ТЕСТА:
        Методика предназначена для оценки субъективного восприятия социальной поддержки респондентом. 
        Она оценивает эффективность и адекватность социальной поддержки по трем аспектам – «семья», «друзья» и «значимые другие».
    Шкалы: 
        Cоциальная поддержка семьи, друзей, значимых других
    """

    def __init__(self, lastname: str = "", name: str = "", surname: str = "", age: int = 0, gender: str = "Мужской") -> None:
        super().__init__(lastname, name, surname, age, gender)
        self.data = self.create_data(test="Шкала социальной поддержки")
        self.rating = self.data['rating']
        self.question = self.data["questions"][self.cur_quest_ind]
        self.family_support = self.friends_support = self.other_support = 0

    def get_result(self) -> dict:
        result = super().get_result()
        result.update({
            "Социальная поддержка семьи": self.family_support,
            "Социальная поддержка друзей": self.friends_support,
            "Социальная поддержка от «значимых других»": self.other_support
        })
        for key, data in self.rating.items():
            for answer in data["answers"]:
                if answer in self.choices:
                    result[key] += data["multiply"]
        return result


def main():
    # l = Leonhard()
    # print(l.get_questions_len())
    # print(l.get_instruction())
    # print(l.question)
    # l.next_quest()
    # print(l.question)
    # l.next_quest()
    # print(l.question)
    # print(l.get_result())

    # s = ScaleOfPersonalAnxiety()
    # print(s.get_instruction())
    # print(s.get_question())
    # s.next_quest()
    # print(s.get_question())

    # c = Cattell()
    # print(c.get_instruction())
    # print(c.get_question())
    # c.next_quest()
    # print(c.get_question())
    # c.next_quest()
    # print(c.get_question())

    # soc = SocialSupportScale()
    # print(soc.get_instruction())
    # print(soc.get_questions_len())
    # print(soc.get_question())
    # soc.next_quest()
    # print(soc.get_question())
    # soc.added_choice(soc.cur_quest_ind)
    # print(soc.get_result())
    # soc.next_quest()
    # soc.added_choice(soc.cur_quest_ind)
    # print(soc.get_result())

    col = ColorRelationship()
    print(col.get_instruction())
    print(col.get_question())

    colkid = ColorRelationshipKid()
    print(colkid.get_instruction())
    print(colkid.get_question())


if __name__ == "__main__":
    main()
