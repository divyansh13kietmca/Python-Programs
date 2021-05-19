

def check_double(number):
    double = number * 2 
    lend = len(str(double)) - str(double).count("0")
    lenn = len(str(number)) - str(number).count("0")
    doub = list(map(str,str(double)))
    numb = list(map(str,str(number)))
    res = check = 0
    if lend == lenn:
        for i in numb:
           if i not in doub:
                 res = 1
        
        for i in range(len(numb)):
            for j in range(len(doub)):
                if i == j and numb[i] != doub[j]:
                    check = 1
               
        if check == 0 or res == 1:
            return False
        else:
            return True

    else:
        return False
#Provide different values for number and test your program
# breakpoint()
print(check_double(100))
