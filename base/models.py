from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, relationship

from sqlalchemy import create_engine
from pyfiglet import figlet_format

Base = declarative_base()


class Admins(Base):

    __tablename__ = "Admins"

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String(length=25), nullable=False)
    password = Column(String(length=128), nullable=False)


class Users(Base):

    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=25), nullable=False)
    father_name = Column(String(length=30), nullable=False)
    last_name = Column(String(length=35), nullable=False)
    age = Column(Integer)
    gender = Column(Boolean(create_constraint=True))  # по умолчанию Мужчина


class Tests(Base):
    """
    Модель таблицы для тестов 

    :class:`id`: № записи теста
    `name`: название теста
    `instruction`: инструкция к тесту
    `questions`: вопросы теста
    """

    __tablename__ = "Tests"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=35), nullable=False)
    instruction = Column(Text(), nullable=False)
    questions = relationship(
        "Questions", backref="Tests", order_by="Questions.id")


class Questions(Base):

    __tablename__ = "Questions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=100), nullable=False)
    answers = relationship(
        "Answers", backref="Questions", order_by="Answers.id")


class Answers(Base):

    __tablename__ = "Answers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    questions_id = Column(ForeignKey("Questions.id"))
    name = Column(String(length=80), nullable=False)


def main():
    logo = figlet_format("Database")
    print(logo)
    while True:

        choice = input("\n[1] Create Database\n"
                       "[0] Exit\n"
                       "Input: ")
        if choice == '1':
            db_name = input(f"[x] New name database: ")
            engine = create_engine(f"sqlite:///{db_name}.db")
            Base.metadata.create_all(engine)
            print(f"[!] Database {db_name}.db create succesfly!")
        elif choice == '0':
            print("Buy!")
            return


if __name__ == "__main__":
    main()
