class Event(DbRecord): ➊
@property
def venue(self):
key = 'venue.{}'.format(self.venue_serial)
return self.__class__.fetch(key) ➋
@property
def speakers(self):
if not hasattr(self, '_speaker_objs'): ➌
spkr_serials = self.__dict__['speakers'] ➍
fetch = self.__class__.fetch ➎
self._speaker_objs = [fetch('speaker.{}'.format(key))
for key in spkr_serials] ➏
return self._speaker_objs ➐
def __repr__(self):
if hasattr(self, 'name'): ➑
cls_name = self.__class__.__name__
return '<{} {!r}>'.format(cls_name, self.name)
else:
return super().__repr__() ➒
