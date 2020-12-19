#in python we can reverse string using [::-1]
#but if we were to implement it in a stack we 
#iterate through the string and push the characters to the stack
#declare an empty string 
# pop elements from the stack 
#append it to the empty string
#stack's LIFO enables us to reverse strings 

from stacks import Stack 

s=Stack()


def reverseStr(string):
 r_string=""
 if len(string) > 0:
    
    for character in string:
        s.push(character)
    while not s.isEmpty():
        r_string += s.pop()
    return r_string
 else:
     print("string is empty")
        

print(reverseStr('feisal'))  
print(reverseStr(''))    
  
   

    
    
    