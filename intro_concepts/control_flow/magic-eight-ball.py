import random

# Initial tutorial had hard coded name and question: https://www.codecademy.com/paths/computer-science/tracks/cspath-cs-101/modules/cspath-python-control-flow/projects/python-magic-8-ball
# Added input methods for making this more dynamic
print('Welcome to magic 8 ball!')
name = input('Enter your name: ')
question = input('What is your question, ' + name + '?:')

answer = ""

random_num = random.randint(1, 9)

if random_num == 1:
    answer = "Yes - definitely."
elif random_num == 2:
    answer = "It is decidedly so."
elif random_num == 3:
    answer = "Without a doubt."
elif random_num == 4:
    answer = "Reply hazy, try again."
elif random_num == 5:
    answer = "Ask again later."
elif random_num == 6:
    answer = "Better not tell you now."
elif random_num == 7:
    answer = "My sources say no."
elif random_num == 8:
    answer = "Outlook not so good."
elif random_num == 9:
    answer = "Very doubtful."
else:
    answer = "Error"


# Stretch goal is to check for empty strings for name and question
if name == '' or question == '':
    print("Thanks for not following the rules!")
else:
   print(name + ' asks: ' + question)
   print('Magic 8 Ball\'s answer: ' + answer) 




