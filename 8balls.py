import random
from datetime import datetime

now = datetime.now()

user_input = input('type what you want a answer for: ')

neg = [
    'Don’t count on it',
    'Outlook not so good',
    'My sources say no',
    'Very doubtful',
    'My reply is no']
neutral = [
    'Reply hazy try again',
    'Better not tell you now',
    'Ask again later',
    'Cannot predict now',
    'Concentrate and ask again'
]
pos = [
    'It is certain',
    'Without a doubt',
    'You may rely on it',
    'Yes definitely',
    'It is decidedly so',
    'As I see it, yes',
    'Most likely',
    'Yes',
    'Outlook good',
    'Signs point to yes'
]

seed_num = 0

for i in range(len(user_input)):
	time = now.strftime("%m%d%Y%H%M%S")
	seed_cal = 1 + int(time)
	seed_num += seed_cal

random.seed(seed_num)

ran_choices = [pos, neutral, neg]
choice = random.choice(ran_choices)

answer = random.choice(choice)
print(answer)