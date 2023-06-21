from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, validator

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    addresses = relationship("Address", back_populates="user")


class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    email = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="addresses")


class UserSchema(BaseModel):
    name: str
    age: int

    @validator('age')
    def age_must_be_positive(cls, v):
        if v < 0:
            raise ValueError('Возраст должен быть положительным числом')
        return v


engine = create_engine('sqlite:///example.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def create_user(name: str, age: int):
    user_schema = UserSchema(name=name, age=age)
    user = User(**user_schema.dict())
    session.add(user)
    session.commit()
    return user


def add_address(user_id: int, email: str):
    address = Address(email=email, user_id=user_id)
    session.add(address)
    session.commit()
    return address


def get_all_users():
    return session.query(User).all()


def get_all_addresses():
    return session.query(Address).all()


def print_table_list():
    print("    1. Пользователи")
    print("    2. Адреса")


def print_actions_list():
    print("    1. Назад к списку таблиц")
    print("    2. Внести данные")
    print("    3. Получить все данные")


def insert_data(table):
    if table == "users":
        name = input("    Введите имя: ")
        age = int(input("    Введите возраст: "))
        try:
            user = create_user(name, age)
            print(f"    Пользователь создан с id {user.id}")
        except ValueError as e:
            print(f"Validation error: {e}")
    elif table == "addresses":
        email = input("    Введите email: ")
        user_id = int(input("    Введите пользовательский id: "))
        address = add_address(user_id, email)
        print(f"    Адрес создан id {address.id}")


def get_all_data(table):
    if table == "users":
        users = get_all_users()
        print("    Пользователи: ")
        for user in users:
            print(f"        id: {user.id}, имя: {user.name}, возраст: {user.age}")
    elif table == "addresses":
        addresses = get_all_addresses()
        print("    Адреса: ")
        for address in addresses:
            print(f"        id: {address.id}, email: {address.email}, пользовательский id: {address.user_id}")


while True:
    print("Список таблиц: ")
    print_table_list()
    table_choice = int(input("    Выберите таблицу: "))

    if table_choice == 1:
        print('Выбрана таблица "Пользователи"')
        table = "users"
    elif table_choice == 2:
        print('Выбрана таблица "Адреса"')
        table = "addresses"

    while True:
        print("Действия с таблицами: ")
        print_actions_list()
        action_choice = int(input("    Выберите действие: "))

        if action_choice == 1:
            break
        elif action_choice == 2:
            insert_data(table)
        elif action_choice == 3:
            get_all_data(table)
