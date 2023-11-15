with open("file1.txt") as file1:

    list1=file1.readlines()
    print(f"List One:\n{list1}")

with open("file2.txt") as file2:

    list2=file2.readlines()
    print(f"List Two:\n{list2}\n")


result=[int(num) for num in list1 if num in list2 ]

print(result)




