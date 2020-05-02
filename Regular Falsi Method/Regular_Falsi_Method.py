import numpy as np

def technique2(x):
    for i in range(1, len(x)):
        if np.isclose(x[i-1], 0, atol = avgval) and np.isclose(x[i], 0, atol= 7):
            print("yes")
    

def technique1(x):
    curr = 0
    near = x[0]
    #find the element nearest to zero    
    for i in range(0, len(x)):
        curr = x[i] * x[i]   
        if curr <= (near * near):      
            near = x[i]
            print(near)
        #two methods. One is check what values are closer to zero
        #second is to just take the first negative value and first positive value closer to zero

def fix_power_sign(equation):
    equation = equation.replace("x", "*x")
    return equation.replace("*x^", "x**")

def f(equation, x_value):
    equation = equation.strip()
    fixed_equation = fix_power_sign(equation.strip())
    nstr = ''
    sign = []
    for i in range(len(fixed_equation)):
        if fixed_equation[i] == '+' :
           nstr += " " 
           sign.append('+')
        elif fixed_equation[i] == '-':
            nstr += " "
            sign.append('-')
        else:
            nstr += fixed_equation[i]
    
    #parts = nstr.strip()
    #nstr = nstr.replace(" ", "")
    parts = nstr.split(" ")
    i=0
    while i < len(parts):
        if parts[i] == '':
            del parts[i]
            i=0
        i += 1
    #parts = parts[i].split('-')
    x_str_value = str(x_value)
    #remove_white_space = (part.remove(" ") for part in parts)
    parts_with_values = (part.replace("x", x_str_value) for part in parts )
    partial_values = (eval(part) for part in parts_with_values)
    value = next(partial_values)
    for j in range(len(sign)):
        if sign[j] == '-':
            value = value - next(partial_values)
        elif sign[j] == '+':
            value = value + next(partial_values)
            
    return value


def NearZeroIndexValues(equation):
    #Evaluate 1 to 4 possible x values that is close to 0 both negative and postive 
    x = []
    for i in range(0,4):
        #print(eval("0**3"))
        x.append(f(equation, i))

    neglist = []
    for number in x:
        if number < 0:
            neglist.append(number)
    poslist = []
    for number in x:
        if number > 0:
            poslist.append(number)

    closestNegValueindex = x.index(max(neglist)) #Maximum negative value will be closer to 0
    #print("index" , closestNegValueindex , "is the nearest neg value")
    closestPosValueindex = x.index(min(poslist)) #Min Positive value will be closer to 0
    #print("index" , closestPosValueindex , "is the nearest Positive value")

    return closestNegValueindex, closestPosValueindex
        
eq = input("Enter equation: ")
a, b = NearZeroIndexValues(eq)
#a, b = 2,3
#if i take a list and add a forloop and increase the list everytime the for loop occurs. I win
iterations = []
for i in range(0,15):    
    x = (a*f(eq,b) - b*f(eq,a))/(f(eq,b) - f(eq,a))
    #a or b =f(x)
    equationfunction = f(eq,x)
    if equationfunction < 0:
        a = x
    elif equationfunction > 0:
        b = x
    iterations.append(x)
Root = False
for i in range(0, len(iterations)):
    print("x",i+1,": ", iterations[i],"\n")
    #check decimal places for close values
    if i+1 > len(iterations) - 1:
        break;
    if np.isclose(iterations[i], iterations[i+1], 0.0001):
        print("Similar till 3 decimal places at x", i+1,"\n")
        print("Root of the equation is", iterations[i],"\n")
        Root = True
    if Root:
        break