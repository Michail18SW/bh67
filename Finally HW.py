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
            raise ValueError('Age must be a positive number')
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
    print("1. Users")
    print("2. Addresses")


def print_actions_list():
    print("1. Back to table list")
    print("2. Insert data")
    print("3. Get all data")


def insert_data(table):
    if table == "users":
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        try:
            user = create_user(name, age)
            print(f"User created with id {user.id}")
        except ValueError as e:
            print(f"Validation error: {e}")
    elif table == "addresses":
        email = input("Enter email: ")
        user_id = int(input("Enter user id: "))
        address = add_address(user_id, email)
        print(f"Address created with id {address.id}")


def get_all_data(table):
    if table == "users":
        users = get_all_users()
        for user in users:
            print(f"id: {user.id}, name: {user.name}, age: {user.age}")
    elif table == "addresses":
        addresses = get_all_addresses()
        for address in addresses:
            print(f"id: {address.id}, email: {address.email}, user_id: {address.user_id}")


while True:
    print_table_list()
    table_choice = int(input("Choose a table by number: "))

    if table_choice == 1:
        table = "users"
    elif table_choice == 2:
        table = "addresses"

    while True:
        print_actions_list()
        action_choice = int(input("Choose an action by number: "))

        if action_choice == 1:
            break
        elif action_choice == 2:
            insert_data(table)
        elif action_choice == 3:
            get_all_data(table)


