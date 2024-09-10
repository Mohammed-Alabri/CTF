Bruteforceme: https://cybertalents.com/challenges/malware/bruteforce-me
* first I analyze the code
```python
ll = [51, 54, 48, 51, 61, 57, 50, 54, 48, 52, 55,
      50, 50, 57, 47, 52, 57, 47, 54, 24, 57, 58, 62]

i = raw_input()  # take input
ss = 0  # var for sum
try:
    for ii in range(0, 46, 2):  # for loop in range 46 seems length of the flag, every two chars
        temp = i[ii:ii+2]  # save first two letters in temp var
        temp = int(temp, 0x10)  # convert it to hex value (0x10 => 16)
        ss += temp  # add temp  value to the sum
        temp >>= 1  # devide temp by two
        # check if temp == to ll[i] (ll seems like encoded flag)
        if temp != ll[ii/2]:
            print "Something is wrong"
    if ss != 2406:  # sum must be equal to 2406 else no
        print ss/0
    print "This flag may or may not work, can you find more ?"

except:  # if letter not hex letters print no
    print "NO"
# flag seems to be in hex value becuase it treat every two chars, and only accept hex lettter

```
* made python code to reverse the encoded flag
```python
from string import ascii_lowercase, digits
ll = [51, 54, 48, 51, 61, 57, 50, 54, 48, 52, 55,
      50, 50, 57, 47, 52, 57, 47, 54, 24, 57, 58, 62]
# flag must only contain a-z, 0-9, _ ,{, }
allowed_letter = ascii_lowercase + digits + "_{}"
# since it takes hex values that is atcule letters so I will treat it as letters
# so the len(flag) == len(ll)
#


def check(txt):  # to minimize the result
    for letter in txt:
        if letter not in allowed_letter:
            return False
    return True

# why recurtion?
# when deviding a number by 2 example:(53 >> 1 same as 53 // 2 = 26) there is two valus gives
# us 26 => (53 >> 1, 52 >> 1) so we need to try every possible combination
# this will give us (2**n) result n= len(ll)


def rec(txt: str, i: int, summ: int):  # recurcive function to get all combinations of result
    if i == len(ll):
        # check if sum == 2406 and txt in allowed_letters
        if summ == 2406 and check(txt):
            print(txt)
        return

    # from above example this try 26*2
    rec(txt + chr(ll[i]*2), i+1,  summ + ll[i]*2)
    # this try 26*2+1
    rec(txt + chr(ll[i]*2+1), i+1,  summ + ll[i]*2+1)


rec('', 0, 0)
```
* this code give us very much result that saticfiy the conditions so I need to minimize the result
```python
from string import ascii_lowercase, digits
ll = [51, 54, 48, 51, 61, 57, 50, 54, 48, 52, 55,
      50, 50, 57, 47, 52, 57, 47, 54, 24, 57, 58, 62]
# flag must only contain a-z, 0-9, _ ,{, }
allowed_letter = ascii_lowercase + digits + "_{}"
# since it takes hex values that is atcule letters so I will treat it as letters
# so the len(flag) == len(ll)
#


def check(txt):  # to minimize the result
    for letter in txt:
        if letter not in allowed_letter:
            return False

    if txt[:5] == 'flag{' and txt[-1] == '}' and 'is_l0st' in txt:  # check if this has flag form
        return True
    return False

# why recurtion?
# when deviding a number by 2 example:(53 >> 1 same as 53 // 2 = 26) there is two valus gives
# us 26 => (53 >> 1, 52 >> 1) so we need to try every possible combination
# this will give us (2**n) result n= len(ll)


def rec(txt: str, i: int, summ: int):  # recurcive function to get all combinations of result
    if i == len(ll):
        # check if sum == 2406 and txt in allowed_letters
        if summ == 2406 and check(txt):
            print(txt)
        return

    # from above example this try 26*2
    rec(txt + chr(ll[i]*2), i+1,  summ + ll[i]*2)
    # this try 26*2+1
    rec(txt + chr(ll[i]*2+1), i+1,  summ + ll[i]*2+1)


rec('', 0, 0)

```
* need to sumbit the  flag that makes sense.
* flag: ```flag{remainder_is_l0st}```
