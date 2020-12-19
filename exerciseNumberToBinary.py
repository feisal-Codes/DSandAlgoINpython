#Algo is 
#divide number by 2
#if it has a reminder , push 1 into the stack else push 0 
#discard the reminder , use the quotient part 
#repeat the procedure until the quotient is 0
#pop the from the stack and store result in a string
from stacks import Stack
s=Stack()
def NumberToBinary(value):
    
    
    if value%2 != 0:
        s.push(1)
        number=value//2
        if number==0:
            return
        else:
            NumberToBinary(number)


    else:
         
        number=value//2
        s.push(0)
        
        
        if number==0:
            return
        else:
            NumberToBinary(number)
     
def main():
 try:
    value=int(input("please enter a postive number to convert to binary: "))
    if value < 0:
        print('sorry we handle positive numbers only for now')
        return
    else:
        NumberToBinary(value)
        i=0
        binary=''
        while i < s.len():
         binary += str(s.pop())
        print(binary)
        return binary
 except(ValueError,ZeroDivisionError):
     print("please enter a positive number")
    
 

main()


