#!/usr/local/bin/python

code = """

print('Hello World')

"""

key = 10

def encrypt(key, code):
    return f"__import__('functools').reduce(str.__add__, [chr(i % 256) for i in [ord(i) + ({key}) for i in {code.__repr__()}]])"

encrypted_code = eval(encrypt(key,code))

print(f"eval({encrypt(-key, encrypted_code)})")