import configparser
from app.main import main
from app.mysqldata import DatabaseSearcher

config = configparser.ConfigParser()
config.read('./config.ini')

database = DatabaseSearcher(host=config['db']['host'],
                            user=config['db']['user'],
                            password=config['db']['password'],
                            database=config['db']['database'])

main(database)
