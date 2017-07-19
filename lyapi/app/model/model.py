from app.db import DBSession

class Model(object):
    def __init__(self):
        self.session = DBSession()

    def __del__(self):
        self.session.close()