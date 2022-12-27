def load_db(db):
raw_data = osconfeed.load()
warnings.warn('loading ' + DB_NAME)
for collection, rec_list in raw_data['Schedule'].items():
record_type = collection[:-1] ➊
cls_name = record_type.capitalize() ➋
cls = globals().get(cls_name, DbRecord) ➌
if inspect.isclass(cls) and issubclass(cls, DbRecord): ➍
factory = cls ➎
else:
factory = DbRecord ➏
for record in rec_list: ➐
key = '{}.{}'.format(record_type, record['serial'])
record['serial'] = key
db[key] = factory(**record) ➑