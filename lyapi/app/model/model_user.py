from app.db.table import TableUser
from app.model import Model
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from app.exception import ExceptionResponse

class ModelUser(Model):
    def find(self):
        result = self.session.query(TableUser).all()
        return result
    def create(self, telephone, password):
        user = TableUser(telephone=telephone, password=password)
        self.session.add(user)
        self.session.commit()

    def find_by_telephone(self, telephone):
        try:
            user = self.session.query(TableUser).filter(TableUser.telephone == telephone).one()
            raise ExceptionResponse(401, "该手机号已注册")
        except NoResultFound:
            return True

    def find_a_user(self, telephone):
        try:
            user = self.session.query(TableUser).filter(TableUser.telephone == telephone).one()
            return user

        except NoResultFound:
            raise ExceptionResponse(400, "您还未注册")

        except MultipleResultsFound:
            raise ExceptionResponse(401, "找到多条结果，请检查")

    def update_access_token(self, user_id, access_token):
        self.session.query(TableUser).filter(TableUser.id == user_id).update({TableUser.access_token:access_token})
        self.session.commit()

    def find_user_by_user_id_and_token(self, user_id, accessToken):
        user = self.session.query(TableUser).filter(TableUser.id == user_id, TableUser.access_token == accessToken).one()



