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
