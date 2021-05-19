def check_anagram(data1,data2):
    data1 = data1.lower()
    data2 = data2.lower()
    string1 = [data1[i] for i in range(len(data1))]
    string2 = [data2[i] for i in range(len(data2))]
    false  = 0
    true = 1
    if len(data1) == len(data2):
        for letter in string1:
            if letter not in string2:
                false = 1
                break
        for letter in string2:
            if letter not in string1:
                false = 1
                break
        if not false:
            for i in range(len(string1)):
                for j in range(len(string2)):
                    if i == j and string1[i] == string2[i]:
                        true = 0
                        continue

        if true and not false:
            return True
        else:
            return False
    else:
        return False

print(check_anagram(data2 = "scller",data1 = "resell"))
