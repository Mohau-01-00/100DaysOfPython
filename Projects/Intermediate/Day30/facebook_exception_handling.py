# eval() function will create a list of dictionaries using the input
facebook_posts = eval(input("Inpute Dictionary :"))

total_likes = 0
# TODO: Catch the KeyError exception
for post in facebook_posts:
 try:
    total_likes = total_likes + post['Likes']
    #There are some posts that do not have likes,except is there to ignore
    #and keep calculating
 except KeyError:
    pass


print(total_likes)

# input
# [{'Likes': 21, 'Comments': 2}, {'Likes': 13, 'Comments': 2, 'Shares': 1}, {'Likes': 33, 'Comments': 8, 'Shares': 3},
#    {'Comments': 4, 'Shares': 2},{'Comments': 1, 'Shares': 1}, 
#    {'Likes': 19, 'Comments': 3}]