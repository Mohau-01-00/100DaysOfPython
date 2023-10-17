# my_dict = {
#            'A': {'x':1,'y':2,'z':3},
#            'B': {'x':4,'y':5,'z':6},
#            'C': {'x':7,'y':8,'z':9}
#           }

# for key, val in my_dict.items():
#     print("Key : {}".format(key))
#     for nested_key, nested_val in val.items():
#         print("{} : {}".format(nested_key,nested_val))



people = {1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
          2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}

#p_id is the first key
#p_info is the 2nd key

for p_id, p_info in people.items():
    print(p_id)
    
    for key in p_info:
        ppl=p_info['Name']
        print(ppl)
        print(key + ':', p_info[key])
        people_age=p_info['Name']

print(type(ppl))
print(ppl)

user=input("Inpur user :")

coffee_price=p_id[user]

