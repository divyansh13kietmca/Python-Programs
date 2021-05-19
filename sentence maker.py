def merge_list(list1, list2):
    merged_data=""
    for i in range(len(list1)-1):
        if list1[i] is not None:
          merged_data += str(list1[i])
        for j in range(len(list2),0,-1):
            if i == len(list2) - 1 -j and list2[j] is not None:
                merged_data += str(list2[j])        
        merged_data += " "
    
    if list1[len(list1)-1] is not None:
        merged_data += str(list1[len(list1)-1])
    if list2[0] is not None:
        merged_data += str(list2[0])
    #write your logic here
    return merged_data

#Provide different values for the variables and test your program
list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']
merged_data=merge_list(list1,list2)
print(merged_data)
