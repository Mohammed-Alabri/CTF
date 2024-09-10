from string import ascii_lowercase, digits
ll = [51, 54, 48, 51, 61, 57, 50, 54, 48, 52, 55,
      50, 50, 57, 47, 52, 57, 47, 54, 24, 57, 58, 62]
# flag must only contain a-z, 0-9, _ ,{, }
allowed_letter = ascii_lowercase + digits + "_{}"
# since it takes hex values that is atcule letters so I will treat it as letters
# so the len(flag) == len(ll)


def check(txt):  # to minimize the result
    for letter in txt:
        if letter not in allowed_letter:
            return False
    return True


def rec(txt: str, i: int, summ: int):
    if i == len(ll):
        if summ == 2406 and check(txt):
            print(txt)
        return

    rec(txt + chr(ll[i]*2), i+1,  summ + ll[i]*2)
    rec(txt + chr(ll[i]*2+1), i+1,  summ + ll[i]*2+1)


rec('', 0, 0)
