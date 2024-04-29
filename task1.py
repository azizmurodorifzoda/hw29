list1=["Black","Maroon","Red","Yellow"] 
list2=["#000000","#FF0000","#800000","FFFF00"]
my_list=[]
for i in range(len(list1)):
    dict={
        "color_name": list1[i],
        "color_code": list2[i]
    }
    my_list.append(dict)
print(my_list)