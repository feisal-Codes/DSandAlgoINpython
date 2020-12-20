# Algo is
# divide number by % 2
# push the remainder
# use the quotient part as new value
# repeat the procedure until the quotient is 0
# pop the from the stack and store result in a string
from stacks import Stack
s = Stack()


def NumberToBinary(value):

    if value == 0:
        return
    remainder = value % 2
    s.push(remainder)
    number = value//2
    NumberToBinary(number)


def main():
    try:
        value = int(
            input("please enter a postive number to convert to binary: "))
        if value < 0:
            print('sorry we handle positive numbers only for now')
            return
        else:
            NumberToBinary(int(value))
            i = 0
            binary = ''
            while i < s.len():
                binary += str(s.pop())
            return binary
    except(ValueError):
        print("please enter a positive number")


print(main())
