import sys
a = 1
b = 0
try:
    print("resource open")
    c = a/b
    print(c)
except ZeroDivisionError as e:
    print("conversion error {}".format(str(e)))
finally:
    print("resource closed")
print("done")