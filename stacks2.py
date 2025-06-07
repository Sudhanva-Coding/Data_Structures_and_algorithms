# python program to find wether a given string has balanced parentheses or not
# approach 1 : stack
# each time when an open parentheses is encountered push it in the stack 
# and when closed parentheses is encountered match it with the to of the stack and pop it
# if the stack is empty at the end return balanced otherwise unbalanced

open_list = ["[", "{", "("]
closed_list = ["]", "}", ")"]

# function to check parentheses
def check(mystr):
    stack = []
    for i in mystr:
        if i in open_list:
            stack.append(i)

        elif i in closed_list:
            pos = closed_list.index(i)
            if ((len(stack) > 0) and 
                (open_list[pos] == stack[len(stack) -1])):
                stack.pop()
            else:
                return "unbalanced"
            
    if len(stack) == 0:
        return "balanced"
    
    else:
        return "unbalanced"
    
# driver code

string = "(hello)"
print(string, "-", check(string))
                    



