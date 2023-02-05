#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser(description="Used to encrypt code to prank people")
parser.add_argument("--code", "-c", metavar="code", type=str, default=None, help="specify the code to be encrypted")
parser.add_argument("--source-file", "-src", metavar="source_file", type=str, default=None, help="specify the source file that will be encrypted")
parser.add_argument("--output-file", "-o", metavar="output_file", type=str, default=None, help="specify the output destination")

# get the code based on the arguments passed to the script

args = parser.parse_args()

code = args.code

if code == None: 
    with open(args.source_file) as source_file:
        code = source_file.read()

if code == None:
    code = input()

# encrypt the code

key = 10

def encrypt(key, code):
    return f"__import__('functools').reduce(str.__add__, [chr(i % 256) for i in [ord(i) + ({key}) for i in {code.__repr__()}]])"

encrypted_code = eval(encrypt(key,code))

output = f"eval({encrypt(-key, encrypted_code)})"

# output the code

if args.output_file != None:
    with open(args.output_file, mode="w") as output_file:
        output_file.write(output)
else:
    print(output)