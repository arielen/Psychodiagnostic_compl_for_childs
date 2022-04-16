from PyQt6 import QtCore, QtGui, QtWidgets
from tests.test import Test, Leonhard_Schmishek
# from tests.test1 import *


class Ui_MainWindow(object):

    def __init__(self) -> None:
        self.Test = Test()
        self.garbage = []

    def setupUi(self, MainWindow) -> None:
        """Создание общих элементов приложения 
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.edt_name = QtWidgets.QLineEdit(self.centralwidget)
        self.edt_name.setGeometry(QtCore.QRect(130, 40, 113, 25))
        self.edt_name.setAccessibleDescription("")
        self.edt_name.setMaxLength(25)
        self.edt_name.setObjectName("edt_name")
        self.edt_father_name = QtWidgets.QLineEdit(self.centralwidget)
        self.edt_father_name.setGeometry(QtCore.QRect(250, 40, 113, 25))
        self.edt_father_name.setMaxLength(35)
        self.edt_father_name.setObjectName("edt_father_name")
        self.edt_last_name = QtWidgets.QLineEdit(self.centralwidget)
        self.edt_last_name.setGeometry(QtCore.QRect(10, 40, 113, 25))
        self.edt_last_name.setMaxLength(35)
        self.edt_last_name.setObjectName("edt_last_name")
        self.edt_age = QtWidgets.QLineEdit(self.centralwidget)
        self.edt_age.setGeometry(QtCore.QRect(10, 70, 113, 25))
        self.edt_age.setValidator(QtGui.QIntValidator())
        self.edt_age.setMaxLength(2)
        self.edt_age.setObjectName("edt_age")
        self.btn_begin = QtWidgets.QPushButton(self.centralwidget)
        self.btn_begin.setGeometry(QtCore.QRect(660, 100, 141, 25))
        self.btn_begin.setObjectName("btn_begin")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 891, 20))
        self.label.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.label.setObjectName("label")

        # combobox choices genders
        self.cbox_gender = QtWidgets.QComboBox(self.centralwidget)
        self.cbox_gender.setGeometry(QtCore.QRect(130, 70, 113, 25))
        self.cbox_gender.setEditable(False)
        self.cbox_gender.setObjectName("cbox_gender")
        for gender in self.Test.get_genders():
            self.cbox_gender.addItem(gender)

        # combobox choices tests
        self.cbox_tests = QtWidgets.QComboBox(self.centralwidget)
        self.cbox_tests.setGeometry(QtCore.QRect(10, 100, 651, 25))
        self.cbox_tests.setObjectName("cbox_tests")
        for test in self.Test.get_tests():
            self.cbox_tests.addItem(test, [f"{test}", f"{test}"])

        # отрисовываем статичный интерфейс
        self.setupUiQuestion()
        self.retranslateUi(MainWindow)

        self.MainWindow = MainWindow

        # update instructions
        self.cbox_tests.currentIndexChanged.connect(self.updateTestCombo)
        self.updateTestCombo(self.cbox_tests.currentIndex())
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def updateTestCombo(self, index) -> None:
        """Обновление интерфейса в зависимости от выбранного теста
        """
        _translate = QtCore.QCoreApplication.translate
        data = {0: {"setup": self.setupTestLeonhardSchmishek,
                    "retranslate": self.retranslateUiLeonhardSchmishek},
                1: {"setup": self.setupTestScalePersonalAnxiety,
                    "retranslate": self.retranslateUiScalePersonalAnxiety},
                2: {"setup": self.setupTestColorEtkind,
                    "retranslate": self.retranslateUiColorEtkind},
                3: {"setup": self.setupTestColorEtkindKids,
                    "retranslate": self.retranslateUiColorEtkindKids},
                4: {"setup": self.setupTestCattell,
                    "retranslate": self.retranslateUiCattell},
                5: {"setup": self.setupTestSocialSupportScale,
                    "retranslate": self.retranslateUiTestSocialSupportScale}}
        self.lbl_instruction.setText(self.Test.get_instruction(index))
        [obj.close() for obj in self.garbage]
        if index in data:
            data[index]["setup"]()
            data[index]["retranslate"](self.MainWindow, _translate)
        [obj.show() for obj in self.garbage]

    def change_edit_user_data(self, params: bool) -> None:
        """Изменение активности пользовательских данных
        :params: принимает bool True для разблокировки, False для блокировки 
        """
        edits = (self.edt_age, self.edt_father_name, self.edt_last_name,
                 self.edt_name, self.cbox_gender, self.cbox_tests)
        for edit in edits:
            edit.setEnabled(params)

    def setupProgressBar(self, max_len: int) -> None:
        """Создание объекта прогресс бара, для отслеживания выполнения 
        """
        # print(max_len)
        self.progressBar = QtWidgets.QProgressBar(
            self.widget, minimum=0, maximum=max_len, objectName="progressBar")
        self.progressBar.setGeometry(QtCore.QRect(50, 320, 700, 20))
        # self.progressBar.setProperty("value", 12)

    def setupProgressBarChanged(self, num_quest: int) -> None:
        """Изменение прогресса от номера вопроса 
        """
        self.progressBar.setProperty("value", num_quest)

    def setupTestLeonhardSchmishek(self) -> None:
        """Создание объектов взаимодействия для теста Leonhard Schmishek
        """
        self.btn_yes = QtWidgets.QPushButton(self.widget)
        self.btn_yes.setGeometry(QtCore.QRect(320, 280, 80, 25))
        self.btn_yes.setObjectName("btn_yes")
        self.btn_no = QtWidgets.QPushButton(self.widget)
        self.btn_no.setGeometry(QtCore.QRect(410, 280, 80, 25))
        self.btn_no.setObjectName("btn_no")
        self.setupProgressBar(max_len=len(self.Test.get_questions(0)))
        self.lbl_question = QtWidgets.QLabel(self.widget)
        self.lbl_question.setGeometry(QtCore.QRect(10, 99, 771, 131))
        self.lbl_question.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_question.setWordWrap(True)
        self.lbl_question.setObjectName("lbl_question")

        self.garbage = [self.btn_yes, self.btn_no,
                        self.progressBar, self.lbl_question]

    def retranslateUiLeonhardSchmishek(self, MainWindow, _translate) -> None:
        """Отрисовка интерфейся посвещенной тесту: 
        Опросник К.Леонгарда – Г. Шмишека для исследования акцентуированных свойств личности
        """
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_yes.setText(_translate("MainWindow", "Да"))
        self.btn_no.setText(_translate("MainWindow", "Нет"))
        self.lbl_question.setText(_translate("MainWindow", "Вопрос"))
        self.btn_yes.clicked.connect(lambda: self.control(self.btn_yes))
        self.btn_no.clicked.connect(lambda: self.control(self.btn_no))

    def setupTestScalePersonalAnxiety(self) -> None:
        """Создание объектов взаимодействия для теста
        2. Шкала личностной тревожности для учащихся 10-16 лет
        """
        self.btn_no = QtWidgets.QPushButton(self.widget)
        self.btn_no.setGeometry(QtCore.QRect(150, 280, 100, 25))
        self.btn_no.setObjectName("btn_no")
        self.btn_little = QtWidgets.QPushButton(self.widget)
        self.btn_little.setGeometry(QtCore.QRect(250, 280, 100, 25))
        self.btn_little.setObjectName("btn_little")
        self.btn_enought = QtWidgets.QPushButton(self.widget)
        self.btn_enought.setGeometry(QtCore.QRect(350, 280, 100, 25))
        self.btn_enought.setObjectName("btn_enought")
        self.btn_much = QtWidgets.QPushButton(self.widget)
        self.btn_much.setGeometry(QtCore.QRect(450, 280, 100, 25))
        self.btn_much.setObjectName("btn_much")
        self.btn_highly = QtWidgets.QPushButton(self.widget)
        self.btn_highly.setGeometry(QtCore.QRect(550, 280, 100, 25))
        self.btn_highly.setObjectName("btn_highly")
        self.setupProgressBar(max_len=len(self.Test.get_questions(1)))

        self.garbage = [self.btn_no, self.btn_little, self.btn_enought,
                        self.btn_much, self.btn_highly, self.progressBar]

    def retranslateUiScalePersonalAnxiety(self, MainWindow, _translate) -> None:
        """Отрисовка интерфейся посвещенной тесту: 
        Опросник К.Леонгарда – Г. Шмишека для исследования акцентуированных свойств личности
        """
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_no.setText(_translate("MainWindow", "Нет"))
        self.btn_little.setText(_translate("MainWindow", "Немного"))
        self.btn_enought.setText(_translate("MainWindow", "Достаточно"))
        self.btn_much.setText(_translate("MainWindow", "Значительно"))
        self.btn_highly.setText(_translate("MainWindow", "Очень"))

    def setupTestColorEtkind(self) -> None:
        self.btn_blue = QtWidgets.QPushButton(self.widget)
        self.btn_blue.setGeometry(QtCore.QRect(50, 210, 175, 50))
        self.btn_blue.setObjectName("btn_blue")
        self.btn_green = QtWidgets.QPushButton(self.widget)
        self.btn_green.setGeometry(QtCore.QRect(225, 210, 175, 50))
        self.btn_green.setObjectName("btn_green")
        self.btn_red = QtWidgets.QPushButton(self.widget)
        self.btn_red.setGeometry(QtCore.QRect(400, 210, 175, 50))
        self.btn_red.setObjectName("btn_red")
        self.btn_yellow = QtWidgets.QPushButton(self.widget)
        self.btn_yellow.setGeometry(QtCore.QRect(575, 210, 175, 50))
        self.btn_yellow.setObjectName("btn_yellow")
        self.btn_violete = QtWidgets.QPushButton(self.widget)
        self.btn_violete.setGeometry(QtCore.QRect(50, 260, 175, 50))
        self.btn_violete.setObjectName("btn_violete")
        self.btn_brown = QtWidgets.QPushButton(self.widget)
        self.btn_brown.setGeometry(QtCore.QRect(225, 260, 175, 50))
        self.btn_brown.setObjectName("btn_brown")
        self.btn_black = QtWidgets.QPushButton(self.widget)
        self.btn_black.setGeometry(QtCore.QRect(400, 260, 175, 50))
        self.btn_black.setObjectName("btn_black")
        self.btn_grey = QtWidgets.QPushButton(self.widget)
        self.btn_grey.setGeometry(QtCore.QRect(575, 260, 175, 50))
        self.btn_grey.setObjectName("btn_grey")
        self.setupProgressBar(max_len=len(self.Test.get_questions(2)))

        self.garbage = [self.btn_blue, self.btn_green, self.btn_red,
                        self.btn_yellow, self.btn_violete, self.btn_brown,
                        self.btn_black, self.btn_grey, self.progressBar]

    def retranslateUiColorEtkind(self, MainWindow, _translate) -> None:
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        colors = {
            "Синий": QtGui.QColor("#1A35E1"), "Зеленый": QtGui.QColor("#1AE142"),
            "Красный": QtGui.QColor("#E11A1A"), "Желтый": QtGui.QColor("#B2E11A"),
            "Фиолетовый": QtGui.QColor("#701AE1"), "Коричневый": QtGui.QColor("#7D530B"),
            "Черный": QtGui.QColor("#000000"), "Серый": QtGui.QColor("#5E5E5E")
        }
        self.btn_blue.setText(_translate("MainWindow", "Синий"))
        self.btn_blue.setPalette(QtGui.QPalette(colors[self.btn_blue.text()]))
        self.btn_green.setText(_translate("MainWindow", "Зеленый"))
        self.btn_green.setPalette(
            QtGui.QPalette(colors[self.btn_green.text()]))
        self.btn_red.setText(_translate("MainWindow", "Красный"))
        self.btn_red.setPalette(QtGui.QPalette(colors[self.btn_red.text()]))
        self.btn_yellow.setText(_translate("MainWindow", "Желтый"))
        self.btn_yellow.setPalette(
            QtGui.QPalette(colors[self.btn_yellow.text()]))
        self.btn_violete.setText(_translate("MainWindow", "Фиолетовый"))
        self.btn_violete.setPalette(
            QtGui.QPalette(colors[self.btn_violete.text()]))
        self.btn_brown.setText(_translate("MainWindow", "Коричневый"))
        self.btn_brown.setPalette(
            QtGui.QPalette(colors[self.btn_brown.text()]))
        self.btn_black.setText(_translate("MainWindow", "Черный"))
        self.btn_black.setPalette(
            QtGui.QPalette(colors[self.btn_black.text()]))
        self.btn_grey.setText(_translate("MainWindow", "Серый"))
        self.btn_grey.setPalette(QtGui.QPalette(colors[self.btn_grey.text()]))

        self.btn_blue.clicked.connect(lambda: self.control(self.btn_blue))
        self.btn_green.clicked.connect(lambda: self.control(self.btn_green))
        self.btn_red.clicked.connect(lambda: self.control(self.btn_red))
        self.btn_violete.clicked.connect(
            lambda: self.control(self.btn_violete))
        self.btn_brown.clicked.connect(lambda: self.control(self.btn_brown))
        self.btn_yellow.clicked.connect(lambda: self.control(self.btn_yellow))
        self.btn_black.clicked.connect(lambda: self.control(self.btn_black))
        self.btn_grey.clicked.connect(lambda: self.control(self.btn_grey))

    def setupTestColorEtkindKids(self) -> None:
        self.setupTestColorEtkind()

    def retranslateUiColorEtkindKids(self, MainWindow, _translate) -> None:
        self.retranslateUiColorEtkind(MainWindow, _translate)

    def setupTestCattell(self) -> None:
        self.garbage = []

    def retranslateUiCattell(self, MainWindow, _translate) -> None:
        pass

    def setupTestSocialSupportScale(self) -> None:
        self.btn_yes = QtWidgets.QPushButton(self.widget)
        self.btn_yes.setGeometry(QtCore.QRect(320, 280, 80, 25))
        self.btn_yes.setObjectName("btn_yes")
        self.btn_no = QtWidgets.QPushButton(self.widget)
        self.btn_no.setGeometry(QtCore.QRect(410, 280, 80, 25))
        self.btn_no.setObjectName("btn_no")
        self.lbl_question = QtWidgets.QLabel(self.widget)
        self.lbl_question.setGeometry(QtCore.QRect(10, 99, 771, 131))
        self.lbl_question.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_question.setWordWrap(True)
        self.lbl_question.setObjectName("lbl_question")
        self.garbage = [self.btn_yes, self.btn_no, self.lbl_question]

    def retranslateUiTestSocialSupportScale(self, MainWindow, _translate) -> None:
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_no.setText(_translate("MainWindow", "Нет"))
        self.btn_yes.setText(_translate("MainWindow", "Да"))
        self.lbl_question.setText(_translate("MainWindow", "Вопрос"))

    def setupUiQuestion(self) -> None:
        """Инициализация основного виджета для тестов
        """
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 130, 800, 350))
        self.widget.setObjectName("widget")
        self.lbl_instruction = QtWidgets.QLabel(self.widget)
        self.lbl_instruction.setGeometry(QtCore.QRect(10, 10, 771, 81))
        self.lbl_instruction.setWordWrap(True)
        self.lbl_instruction.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_instruction.setObjectName("lbl_instruction")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 895, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

    def retranslateUi(self, MainWindow) -> None:
        """Отрисовка основного интерфейса
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.edt_name.setPlaceholderText(_translate("MainWindow", "Имя"))
        self.edt_father_name.setPlaceholderText(
            _translate("MainWindow", "Отчество"))
        self.edt_last_name.setPlaceholderText(
            _translate("MainWindow", "Фамилия"))
        self.edt_age.setPlaceholderText(_translate("MainWindow", "Возраст"))
        self.btn_begin.setText(_translate("MainWindow", "Начать тестирование"))
        self.label.setText(_translate("MainWindow", "Психодиагностический комплекс для детей (или автоматизированное тестирование личности детей), оказавшихся в трудной жизненной ситуации)\n"
                                      ""))

        self.add_functions()

    def add_functions(self) -> None:
        """Добавляем функции к кнопкам
        """
        self.btn_begin.clicked.connect(
            lambda: self.control(self.btn_begin)
        )

    def control(self, btn: QtWidgets.QPushButton) -> None:
        """Основная функция контроля приложения
        """
        def check_data():
            return "" not in (val.text() for val in (self.edt_age, self.edt_father_name, self.edt_last_name, self.edt_name))

        if btn == self.btn_begin:
            if check_data():
                self.Test.set_data(
                    last_name=self.edt_last_name.text(),
                    name=self.edt_name.text(),
                    surname=self.edt_father_name.text(),
                    gender=self.cbox_gender.itemText(
                        self.cbox_gender.currentIndex()),
                    age=int(self.edt_age.text())
                )
                self.change_edit_user_data(params=False)
                self.Test.init_test(cur_test=self.cbox_tests.currentIndex())
            else:
                print(self.cbox_tests.currentIndex())
                return self.showErrorOk("Не все данные введены !")
        try:
            for btn_col in (self.btn_blue, self.btn_black, self.btn_yellow,
                            self.btn_grey, self.btn_green, self.btn_brown,
                            self.btn_red, self.btn_violete):
                if btn is btn_col:
                    print(btn.text())
        except:
            pass
        for btn_bool in (self.btn_yes, self.btn_no):
            if btn is btn_bool:
                print(self.Test.cur_test)

    def showErrorOk(self, text: str = "") -> None:
        """Простой вывод ошибок с кнопкой "Ok" 
        """
        reply = QtWidgets.QMessageBox()
        reply.setText(text)
        reply.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        reply.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        reply.exec()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
