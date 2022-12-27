from datetime import datetime
now = datetime.now()
print(format(now, '%I:%M:%p'))#hours minutes seconds
print("It's now {:%I:%M:%p}".format(now))#IDK THIS