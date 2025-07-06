import os
import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'St. Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

os.chdir('C:\\Users\\Katherine\\Downloads\\Python\\Automate\\Capital Quizzes') # i think windows has learned to handle forward slashes so i coulda done os.chdir('C:/Users/Katherine/Downloads/Python/Automate/Capital Quizzes')
os.makedirs('./result', exist_ok = True)
for i in range(10):
    items = list(capitals.items())
    random.shuffle(items)
    capitals = dict(items)

    with open(f'./result/quiz{i}.txt', 'w') as f: # here i accidentally used forward slashes and it worked
        for j, (key, val) in enumerate(capitals.items()):
            choices = {val}
            while len(choices) < 4:
                choices.add(random.choice(list(capitals.values())))
            f.write(f'{j}. {key}\n')
            for letter in ('Z','a','b','c'):
                f.write(f'\t{letter}. {choices.pop()}\n')
            f.write('\n')
        print('quiz created')
print('done')