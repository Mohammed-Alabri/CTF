Forgot the password: https://ctf.eoman.com/competitions/public/cryptography/forgot_the_password

* first crack the zip file using john
```bash
zip2john flag.zip > hash
john hash -w=/usr/share/wordlists/rockyou.txt --show
```
* I got the password ```mystery```

* I got flag.txt file that have random letter and message, tried to remove lower case chars using python code
```python
file = open('flag.txt')

line = file.read().splitlines()[9]  # need only line that has the words
res = ""
for letter in line:
    if letter.isupper():  # check if letter is upper case
        res += letter

print(res)
```

* by running code the flag appears ```YOUARESUPERB```
