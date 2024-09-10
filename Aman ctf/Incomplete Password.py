from hashlib import sha1
from string import printable
hashh = "827d1057ad7258b180efca5e9cc25795a1a5f622"

password = "Om@nYg"


def rec(password: str):
    if len(password) == 10:  # base case pass not exceed 9 letterrs
        return
    if sha1(password.encode()).hexdigest() == hashh:  # checking  if hash equal
        print(password)
        exit()
    for letter in printable:  # do recurion for all printable chars
        rec(password+letter)


rec(password)  # call recursive function
