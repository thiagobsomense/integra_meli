import logging
from sqlalchemy.orm import Session
from database.conn import engine, LogsML


try:
    session = Session(engine)
except Exception as err:
    print(f'Não foi possível conectar ao banco de dados. Erro: {err}')


class CustomHandler(logging.StreamHandler):
    def __init__(self, session):
        super().__init__()
        self.session = session

    def emit(self, record):
        if record:
            values = {
                'user_id': record.user_id,
                'step': record.funcName,
                'body': record.body,
                'status': record.levelname,
                'message': record.msg,
                'init_at': record.init_at,
                'end_at': record.end_at,
            }
            self.session.add(LogsML(**values))
            self.session.commit()


logger = logging.Logger('test')
logger.setLevel(logging.DEBUG)
customhandler = CustomHandler(session)
logger.addHandler(customhandler)
