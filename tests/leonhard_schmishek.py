import json


class Leonhard_Schmishek:

    def __init__(self) -> None:
        """Класс для проверки тестирования 

        hyperthymia Гипертимность
        lateness Застревание
        emotivity Эмотивность
        pedantry Педантичность
        anxiety Тревожность
        cyclothymicity Циклотимность
        demonstrativeness Демонстративность
        excitability Возбудимость
        distimism Дистимичность
        exaltation Экзальтированность
        """
        self.data = self.__create_data("Леонгарда-Шмишека")
        self.rating = self.data['rating']
        self.hyperthymia = self.lateness = 0
        self.emotivity = self.pedantry = 0
        self.anxiety = self.cyclothymicity = 0
        self.demonstrativeness = self.excitability = 0
        self.distimism = self.exaltation = 0
        self.choice_variants = []

    def __create_data(self, name_test,) -> dict:
        with open("tests/tests_data.json", 'r', encoding="utf-8") as f:
            return json.load(f)[name_test]

    def added_choice(self, question: str) -> None:
        """Принимает номер вопроса и добавляет его в self.choice_variants
        Примечание: Первый элемент = 1
        """
        self.choice_variants.append(int(question))

    def get_result(self) -> dict:
        """Возвращает словарь с результатами, где ключ = Характеристике,
        а значение кол-ву очков. 
        """
        result = {"Гипертимность": self.hyperthymia, "Застревание": self.hyperthymia,
                  "Эмотивность": self.emotivity, "Педантичность": self.pedantry,
                  "Тревожность": self.anxiety, "Циклотимность": self.cyclothymicity,
                  "Демонстративность": self.demonstrativeness, "Возбудимость": self.excitability,
                  "Дистимичность": self.distimism, "Экзальтированность": self.exaltation}
        # проверяем результаты
        for key, data in self.rating.items():
            for answer in data['answers']:
                if (answer > 0 and answer in self.choice_variants) or (answer < 0 and answer not in self.choice_variants):
                    result[key] += data['multiply']
        data = self.check_accentuated(result)
        return result

    def check_accentuated(self, result: dict) -> dict:
        """Проверка акцентируемых черт 
        """
        res = {}
        for feature, value in result.items():
            if value >= 24:
                res.update({feature: "Требует дополнительного обследования"})
            elif value > 12:
                res.update({feature: "Акцентируемая черта"})
            else:
                res.update({feature: "В пределах нормы"})
        return res

    def __str__(self) -> str:
        return str(pprint.pformat(self.rating))


def main():
    d = Leonhard_Schmishek()
    print(d.get_result())


if __name__ == "__main__":
    main()
