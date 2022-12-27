import shelve
db = shelve.open(DB_NAME)
if CONFERENCE not in db:
    load_db(db)

speaker = db['speaker.3471']
print(type(speaker))
print(speaker.name, speaker.twitter)
db.close()