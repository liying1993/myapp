from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import check_password_hash, generate_password_hash

Base = declarative_base()

class TableUser(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    telephone = Column(String)
    access_token = Column(String)

    def __init__(self,telephone, password):
        self.telephone = telephone
        self.password = self.set_password(password)


    def set_password(self, password):
        self.hash_password = generate_password_hash(password)
        return self.hash_password

    def check_password(self, password):
        return check_password_hash(self.hash_password, password)

    def to_dict(self):
        return {
            "id":self.uid,
            "username":self.username,
            "password":self.password,
            "telephone": self.telephone,
            "access_token": self.access_token
        }
