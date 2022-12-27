from osconfeed import load
raw_feed = load()
feed = FrozenJSON(raw_feed)
print(len(feed.Schedule.keys()))
for key, value in sorted(feed.Schedule.items()):
    print('{:3} {}'.format(len(value), key))
feed.Schedule.speakers[-1].name
talk = feed.Schedule.events[40]
print(type(talk))
print(talk.name)
print(talk.speakers)
print(talk.flavor)
