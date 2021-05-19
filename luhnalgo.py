def validate_credit_card_number(card_number):
    #start writing your code here
    num = str(card_number)
    # step 1a
    double = []
    # values = []
    # above_9 = []
    # below_9 = []
    for i in range(len(num)-2,-1,-2):
        # values.append(num[i])
        if int(num[i])*2 > 9:
            temp = int(num[i])*2
            # above_9.append(temp)
            s = 0
            while temp > 0:
                rem = temp % 10
                s += rem
                temp //= 10
            double.append(s)
        else:
            # below_9.append(int(num[i]))
            double.append((int(num[i])*2))
    # print(num)
    # print(f"value = {values}")
    # print(f"above_9 = {above_9}")
    # print(f"before_9 = {below_9}")
    # print(f"double = {double}")

    # step 1b
    step1_sum = sum(double)
    # print(f"step1_sum = {step1_sum}")

    # step 2a
    step2_sum = 0
    # step2_val = []
    for i in range(1,len(num),2):
        # step2_val.append(num[i])
        step2_sum += int(num[i])
    # print(f"step2_val = {step2_val}")
    # print(f"step2_sum = {step2_sum}")

    #step 2b
    total = step1_sum + step2_sum
    # print(f"total = {total}")
    #step 3
    if total % 10 == 0:
        return True
    else:
        return False


card_number=5239512608615007  #1456734512345698 #4539869650133101  #1456734512345698 # #5239512608615007
result=validate_credit_card_number(card_number)
if(result):
    print("credit card number is valid")
else:
    print("credit card number is invalid")

