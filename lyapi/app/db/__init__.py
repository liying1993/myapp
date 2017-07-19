from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/flaskr')
DBSession = sessionmaker(bind=engine)
