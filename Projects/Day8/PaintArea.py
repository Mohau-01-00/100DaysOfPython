# Write your code below this line 👇
import math
#area=heigh*width/coverage of paint
def paint_calc(height,width,cover):
  num_cans=(height*width)/cover
  round_up_cans=math.ceil(num_cans)
  print(f"You will need {round_up_cans} cans of paint")

# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of the wall :\n")) # Height of wall (m)
test_w = int(input("Width of the wall :\n")) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

