from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TableUser(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

    def __init__(self,username, password):
        self.username = username
        self.password = password

    def to_dict(self):
        return {
            "id":self.uid,
            "username":self.username,
            "password":self.password
        }