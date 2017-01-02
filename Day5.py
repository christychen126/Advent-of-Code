from hashlib import md5
from itertools import count, islice



key = 'wtnhxymk'
def decrypting_code(key):

    result = ''
    hex = lambda i: md5(key + str(i)).hexdigest()
    results = (hex(i)[5] for i in count() 
    if hex(i).startswith('00000'))

    print ''.join(islice(results, 8))

# decrypting_code(key)

def decrypting_code_2(key):

    result = [None] * 8
    hex = lambda i: md5(key + str(i)).hexdigest()
    for i in count():
        hash = hex(i)
        if hash.startswith('00000'):
            try:
                ind, char = int(hash[5]), hash[6]
            except:
                continue
            if ind not in range(0, 8) or result[ind]:
                continue
                
            result[ind] = char
            if all(result):
                print ''.join(result)
                break

decrypting_code_2(key)
