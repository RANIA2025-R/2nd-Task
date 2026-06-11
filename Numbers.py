Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Numbers.py")
Numbers.py
>>> numbers = list(range(1, 21))
...
... divisible_by_3 = []
...
... for num in numbers:
...     if num % 3 == 0:
...         divisible_by_3.append(num)
...
... print("Numbers divisible by 3:", divisible_by_3)
...
