cafe = bytes('café', encoding='utf-8')
print(cafe)
print(cafe[0])
print(cafe[:1])
cafe_arr = bytearray(cafe)
print(cafe_arr)
print(cafe_arr[-1:])


doge = bytes('doge', encoding='utf-8')
doge_arr = bytearray(doge)
print(doge_arr)
print(doge_arr[-1:])