import random
from tkinter.font import names

famous_accounts = [
    {
        'name': 'Cristiano Ronaldo',
        'followers': 620,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Lionel Messi',
        'followers': 500,
        'description': 'Footballer',
        'country': 'Argentina'
    },
    {
        'name': 'Selena Gomez',
        'followers': 430,
        'description': 'Singer and Actress',
        'country': 'USA'
    },
    {
        'name': 'Kylie Jenner',
        'followers': 400,
        'description': 'Entrepreneur and Model',
        'country': 'USA'
    },
    {
        'name': 'Dwayne Johnson',
        'followers': 390,
        'description': 'Actor and Wrestler',
        'country': 'USA'
    },
    {
        'name': 'Ariana Grande',
        'followers': 380,
        'description': 'Singer',
        'country': 'USA'
    },
    {
        'name': 'Kim Kardashian',
        'followers': 360,
        'description': 'Reality TV Star',
        'country': 'USA'
    },
    {
        'name': 'Beyonce',
        'followers': 320,
        'description': 'Singer',
        'country': 'USA'
    },
    {
        'name': 'Khloe Kardashian',
        'followers': 310,
        'description': 'Reality TV Star',
        'country': 'USA'
    },
    {
        'name': 'Justin Bieber',
        'followers': 290,
        'description': 'Singer',
        'country': 'Canada'
    },
    {
        'name': 'Taylor Swift',
        'followers': 280,
        'description': 'Singer and Songwriter',
        'country': 'USA'
    },
    {
        'name': 'Neymar Jr',
        'followers': 220,
        'description': 'Footballer',
        'country': 'Brazil'
    },
    {
        'name': 'Virat Kohli',
        'followers': 260,
        'description': 'Cricketer',
        'country': 'India'
    },
    {
        'name': 'Zendaya',
        'followers': 190,
        'description': 'Actress',
        'country': 'USA'
    },
    {
        'name': 'Instagram',
        'followers': 650,
        'description': 'Social Media Platform',
        'country': 'USA'
    }
]
score = 0
running = True
while running:
    account_one = random.choice(famous_accounts)
    account_two = random.choice(famous_accounts)
    while account_one == account_two:
        account_two = random.choice(famous_accounts)
        a = account_one['name']
        b = account_two['name']
        c = account_one['country']

        user_choice=input(f"who has the more followers on instagram\n {a} from {c}  or {b} from {c} "
                          f", press  a or b \n" ).lower()
        if user_choice == a.lower() or b.lower():
                if account_one['followers']>account_two['followers']:
                 print("you answer is correct")
                 score=score+1
                 print(f"your scode is {score}")
                else:
                    print(f"you answer is wrong  your score is {score}")
                    running = False
                    break







