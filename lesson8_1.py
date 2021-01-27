import hashlib


def fun_substring(substring):
    arrey_pattern = [hashlib.sha256(''.encode('utf-8')).hexdigest(), hashlib.sha256(' '.encode('utf-8')).hexdigest(), hashlib.sha256(substring.encode('utf-8')).hexdigest()]
    arrey_hash = []
    for i in range(len(substring)):
        n = i
        while n <= len(substring):
            if hashlib.sha256(substring[i:n].encode('utf-8')).hexdigest() not in arrey_hash and hashlib.sha256(substring[i:n].encode('utf-8')).hexdigest() not in arrey_pattern:
                arrey_hash.append(hashlib.sha256(substring[i:n].encode('utf-8')).hexdigest())
            n += 1
    return len(arrey_hash)


count_substring = fun_substring(input('Введите строку: '))
print(count_substring)
