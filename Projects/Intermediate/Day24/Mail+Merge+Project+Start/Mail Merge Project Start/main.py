# : Create a letter using starting_letter.txt 
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".


with open("Input/Letters/starting_letter.txt", "r") as starting_letter:

     contents=starting_letter.read()
     #contents is the strings/words in starting letter
     print(contents)

with open("Input/Names/invited_names.txt", "r") as invited_names:
          names=invited_names.read()
          name_list=list(names.split("\n") )
          print(name_list)



for invited_name in name_list:
     new_name = contents.replace("[name]",invited_name)
     with open(f"Output/ReadyToSend/letter_for_{invited_name}.txt","w") as f:
        
  
      f.write(new_name)



     print(new_name)


