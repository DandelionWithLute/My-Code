octets = b'Montr\xe9al'
print(octets.decode('cp1252'))
print(octets.decode('iso8859_7'))
print(octets.decode('koi8_r'))
print(octets.decode('utf-8', errors='ignore'))
print(octets.decode('utf-8'))