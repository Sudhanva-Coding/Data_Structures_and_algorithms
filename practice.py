list1 = [2,4,5,6,7,]

m1 = max(list1)
m2 = min(list1)

print(m1)
print(m2)


#def fibonacci(n):
    # base cases
    #if n == 0:
    # return 0
    #elif n == 1:
        #return 1

    # recursive case
    #else:
        #return fibonacci(n-1) + fibonacci(n-2)

# using recursin calculate the power of a number

def exponent(n, x):
    if x == 0:
        return 1
    elif x == 1:
        return n
    else:
        return (n*exponent(n, x-1))
        
if __name__ == "__main__":
    n = 4
    x = 2

    print(exponent(n, x))


# using type function call a function at run time

import types
code = compile("def greet(name): return f'Hello, {name}!'", "<string>", "exec")
d = {}
exec(code, d) # execute the compiled code in a seperate name space
msg = d["greet"] #  retrieve the function from the name space
print(msg("geeks"))