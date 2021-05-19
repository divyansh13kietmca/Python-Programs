
def find_duplicates(list_of_numbers):
    result = []
    for i in range(len(list_of_numbers)):
        for j in range(i+1,len(list_of_numbers)):
            if list_of_numbers[i] == list_of_numbers[j] and list_of_numbers[i] not in result:
                result.append(list_of_numbers[i])
                break

    return  result
list_of_numbers=[1,2,3,4]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)
