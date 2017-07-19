from app.db.table import TableUser
from app.model import Model
from sqlalchemy.orm.exc import NoResultFound

class ModelUser(Model):
    def find(self):
        result = self.session.query(TableUser).all()
        return result

