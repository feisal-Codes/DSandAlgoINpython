from stacks import Stack


#algo is 
#parse through the string
#check if it's an opening bracket and push it to 
#the stack 
#check if its a closing bracket , pop the last element from 
#the stack and compare if they match we conclude it's a balanced 
#bracket and move on 
#at the end of the iteration the stack would be empty for 
#a balanced example of brackets and left with some elements 
#for an unbalanced

def isBracketBalanced(valueString):
    s= Stack()
    index=0
    isBalanced=True
   
    while index < len(valueString) and isBalanced:
       
        character =valueString[index]
        if character in "([{":
           s.push(character)
        else:
           if s.isEmpty():
               isBalanced=False
           else:
               top=s.pop()
               if not isMatch(top,character):
                   isBalanced = False
        
        index+=1
    if s.isEmpty() and isBalanced:
        return True
    else:
        return False
    
    
    
    
   

def isMatch(v1,v2):
    if v1 == "(" and v2 == ")":

        return True
    elif v1 == "{" and v2 == "}":

        return True
    elif v1 == "[" and v2 == "]":

        return True
    else:
        return False




print(isBracketBalanced("()"))

print(isBracketBalanced("({[]}))"))
print(isBracketBalanced("({[]}))(("))












