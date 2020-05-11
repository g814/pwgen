from random import randint, choice
import argparse
import string
import sys

parser = argparse.ArgumentParser(description="Generate some passwords.")

arg_list = parser.add_mutually_exclusive_group()

arg_list.add_argument('-f', '--forever', action="store_true", help='Run until Ctrl-C.')

arg_list.add_argument('-c', '--count', metavar="count", type=int, nargs="+", help="Number of passwords to generate. Default is 25.")

arg_list.add_argument('-l', '--length', metavar="length", type=int, nargs="+", help="Length of passwords to generate. Default is a random number from 10 to 35")

args = parser.parse_args()

letters_lowercase = list(string.ascii_lowercase)
letters_uppercase = list(string.ascii_uppercase)
symbols = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', '{', ']', '}', '\\', '|', ';', ':', "'", '"', ',' '<', '.', '>', '/']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
length = randint(10, 35)

total = letters_uppercase + letters_lowercase + symbols + numbers

if args.forever:
    try:
        while True:
            total_length = length
            while total_length:
                print(choice(total), end="")
                total_length = total_length - 1
            print("")
            length = randint(10, 35)
    except KeyboardInterrupt:
        sys.exit(0)

if args.count:
    try:
        for i in range(1, int(args.count[0]) + 1):
            total_length = length
            while total_length:
                print(choice(total), end="")
                total_length = total_length - 1
            print("")
            length = randint(10, 35)
        sys.exit(0)
    except KeyboardInterrupt:
        sys.exit(0)

if args.length:
    length = args.length[0]
    try:
        for i in range(1, 25):
            total_length = length
            while total_length:
                print(choice(total), end="")
                total_length = total_length - 1
            print("")
        sys.exit(0)
    except KeyboardInterrupt:
        sys.exit(0)

try:
    for i in range(1, 25):
        total_length = length
        while total_length:
            print(choice(total), end="")
            total_length = total_length - 1
        print("")
        length = randint(10, 35)
except KeyboardInterrupt:
    sys.exit(0)
