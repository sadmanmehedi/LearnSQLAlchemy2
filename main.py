from sqlalchemy import ForeignKey, Column, Integer, String, CHAR, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Person(Base):
    __tablename__ = "people"

    ssn = Column("ssn", Integer, primary_key=True)
    firstname = Column("FirstName", String)
    lastname = Column("LastName", String)
    age = Column("Age", Integer)

    def __init__(self, ssn, firstname, lastname, age):
        self.ssn = ssn
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def __repr__(self):
        return f"{self.ssn},{self.firstname},{self.lastname},{self.age}"

class Thing(Base):
    __tablename__ = "things"

    tid = Column("tid", Integer, primary_key=True)
    description = Column("description", String)
    owner = Column(Integer, ForeignKey("people.ssn"))

    def __init__(self, tid, description, owner):
        self.tid = tid
        self.description = description
        self.owner = owner

    def __repr__(self):
        return f"{self.tid},{self.description}{self.owner}"


engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

person = Person(43, "Sadman", "Sivan", 23)
session.add(person)
session.commit()

p1 = Person(19, "Bhagina", "Zaira", 23)
p2 = Person(20, "Faisal Mehedi", "Shammo", 24)
p3 = Person(21, "Sifat Laila", "Tanvi", 25)

session.add(p1)
session.add(p2)
session.add(p3)

session.commit()

sivan = Thing(22, "Allah Help me", 23)
session.add(sivan)
session.commit()
