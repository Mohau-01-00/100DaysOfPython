import pandas as pd


import pandas
df= pd.read_csv("nato_phonetic_alphabet.csv")

print(df)

nato_phonetic={row.letter:row.code for (index,row) in df.iterrows()}

print(nato_phonetic)

#input a word
should_continue=True
while should_continue:
    word=input("Enter a word :").upper()  #Mohau
    nato_output=[nato_phonetic[letter] for letter in word]

    print(nato_output)
    if word=="E":
        should_continue=False