class MissingDatabaseError(RuntimeError):
"""需要数据库但没有指定数据库时抛出。""" ➊
class DbRecord(Record): ➋
__db = None ➌
@staticmethod ➍
def set_db(db):
DbRecord.__db = db ➎
@staticmethod ➏
def get_db():
return DbRecord.__db
11
11
@classmethod ➐
def fetch(cls, ident):
db = cls.get_db()
try:
return db[ident] ➑
except TypeError:
if db is None: ➒
msg = "database not set; call '{}.set_db(my_db)'"
raise MissingDatabaseError(msg.format(cls.__name__))
else: ➓
raise
def __repr__(self):
if hasattr(self, 'serial'): ⓫
cls_name = self.__class__.__name__
return '<{} serial={!r}>'.format(cls_name, self.serial)
else:
return super().__repr__() ⓬