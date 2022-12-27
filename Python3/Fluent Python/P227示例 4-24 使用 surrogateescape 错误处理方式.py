import os
print( os.listdir('.'))
#['abc.', 'digits-of-π.']
print( os.listdir(b'.'))
#[b'abc.', b'digits-of-\xcf\x80.']
print(pi_name_bytes = os.listdir(b'.')[1])
print(pi_name_str = pi_name_bytes.decode('ascii', 'surrogateescape'))
print(pi_name_str)
#'digits-of-\udccf\udc80.txt'
print(pi_name_str.encode('ascii', 'surrogateescape'))
#b'digits-of-\xcf\x80.txt