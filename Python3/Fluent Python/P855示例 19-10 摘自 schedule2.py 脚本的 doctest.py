>>> DbRecord.set_db(db) ➊
>>> event = DbRecord.fetch('event.33950') ➋
>>> event ➌
<Event 'There *Will* Be Bugs'>
>>> event.venue ➍
<DbRecord serial='venue.1449'>
>>> event.venue.name ➎
'Portland 251'
>>> for spkr in event.speakers: ➏
... print('{0.serial}: {0.name}'.format(spkr))
...
speaker.3471: Anna Martelli Ravenscroft
speaker.5199: Alex Martelli
