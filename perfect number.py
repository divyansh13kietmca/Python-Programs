def check_perfect_number(number):
    perfect_sum = []
    for i in range(1,number):
        if number % i == 0:
            perfect_sum.append(i)
    if sum(perfect_sum) == number:
        return True

    else:
        return False
def check_perfectno_from_list(no_list):
    results = []
    for num in no_list:
        if check_perfect_number(num) and num is not 0:
            results.append(num)
    return results
# print(check_perfect_number(28))
perfectno_list=check_perfectno_from_list([18,6,4,2,1,28])
print(perfectno_list)

