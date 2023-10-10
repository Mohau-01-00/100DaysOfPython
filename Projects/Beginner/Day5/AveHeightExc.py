#You are going to write a program that calculates the average student height from a List of heights.

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_height=0
for height in student_heights:
 total_height+=height #or total_height=total_height+height
print(total_height)

num_of_students=0
for student in student_heights:
 num_of_students+=1
print(num_of_students)

ave_height=round(total_height/num_of_students)
print(ave_height)
