from PyQt6 import QtCore, QtGui, QtWidgets
from tests.test import Test


class Ui_MainWindow(object):

    def __init__(self) -> None:
        self.Test = Test()

    def setupUi(self, MainWindow):
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
        self.edt_age.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.edt_age.setInputMask("")
        self.edt_age.setText("")
        self.edt_age.setMaxLength(2)
        self.edt_age.setObjectName("edt_age")

        # combobox choices genders
        self.cbox_gender = QtWidgets.QComboBox(self.centralwidget)
        self.cbox_gender.setGeometry(QtCore.QRect(130, 70, 113, 25))
        self.cbox_gender.setEditable(False)
        self.cbox_gender.setObjectName("cbox_gender")
        for gender in self.Test.get_genders():
            self.cbox_gender.addItem(gender)

        self.btn_begin = QtWidgets.QPushButton(self.centralwidget)
        self.btn_begin.setGeometry(QtCore.QRect(660, 100, 141, 25))
        self.btn_begin.setObjectName("btn_begin")

        # combobox choices tests
        self.cbox_tests = QtWidgets.QComboBox(self.centralwidget)
        self.cbox_tests.setGeometry(QtCore.QRect(10, 100, 651, 25))
        self.cbox_tests.setObjectName("cbox_tests")
        for test in self.Test.get_tests():
            self.cbox_tests.addItem(test)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 891, 20))
        self.label.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.label.setObjectName("label")
        # отрисовываем статичный интерфейс
        self.setupUiQuestion()
        self.retranslateUi(MainWindow)

        self.retranslateUiQuestion(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setupUiQuestion(self) -> None:
        """Создание элементов тестовой части 
        """
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 130, 791, 321))
        self.widget.setObjectName("widget")
        self.btn_yes = QtWidgets.QPushButton(self.widget)
        self.btn_yes.setGeometry(QtCore.QRect(320, 280, 80, 25))
        self.btn_yes.setObjectName("btn_yes")
        self.btn_no = QtWidgets.QPushButton(self.widget)
        self.btn_no.setGeometry(QtCore.QRect(410, 280, 80, 25))
        self.btn_no.setObjectName("btn_no")
        self.progressBar = QtWidgets.QProgressBar(self.widget)
        self.progressBar.setGeometry(QtCore.QRect(60, 280, 118, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.lbl_instruction = QtWidgets.QLabel(self.widget)
        self.lbl_instruction.setGeometry(QtCore.QRect(10, 10, 771, 81))
        self.lbl_instruction.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_instruction.setObjectName("lbl_instruction")
        self.lbl_question = QtWidgets.QLabel(self.widget)
        self.lbl_question.setGeometry(QtCore.QRect(10, 99, 771, 131))
        self.lbl_question.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_question.setObjectName("lbl_question")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 895, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

    def retranslateUiInstruction(self, MainWindow):
        self.lbl_instruction.setText(_translate(
            "MainWindow", self.Test.get_instruction()))
        pass

    def retranslateUiQuestion(self, MainWindow):
        """Отрисовка интерфейся посвещенной тесту: 
        Опросник К.Леонгарда – Г. Шмишека для исследования акцентуированных свойств личности
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_yes.setText(_translate("MainWindow", "Да"))
        self.btn_no.setText(_translate("MainWindow", "Нет"))
        self.lbl_instruction.setText(_translate(
            "MainWindow", self.Test.get_instruction()))
        self.lbl_question.setText(_translate("MainWindow", "Вопрос"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.edt_name.setPlaceholderText(_translate("MainWindow", "Имя"))
        self.edt_father_name.setPlaceholderText(
            _translate("MainWindow", "Отчество"))
        self.edt_last_name.setPlaceholderText(
            _translate("MainWindow", "Фамилия"))
        self.edt_age.setPlaceholderText(_translate("MainWindow", "Возраст"))
        self.btn_begin.setText(_translate("MainWindow", "Начать тестирование"))

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
                print('letsgo')
            else:
                self.showErrorOk("Не все данные введены !")

    def showErrorOk(self, text: str = ""):
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
