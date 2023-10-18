from sqlalchemy import create_engine

username = 'root'
password = '368549'
server = 'localhost'
port = 3306
database = 'db_analize'

str_conn = f'mysql+pymysql://{username}:{password}@{server}:{port}/{database}'
engine = create_engine(str_conn)