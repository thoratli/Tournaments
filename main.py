import configparser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import main

config = configparser.ConfigParser()
config.read('./config.ini')


dsn = 'mysql+mysqlconnector://' + config['db']['user'] + ':' + config['db']['password'] + '@' + config['db']['host'] + '/' + config['db']['database']

engine = create_engine(dsn)

sm = sessionmaker()
sm.configure(bind=engine)

session = sm()

main(session)
