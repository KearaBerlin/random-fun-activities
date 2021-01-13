import random

adjectives = ['Quickly', 'Seriously', 'Slowly', 'With fear,', 'Blindfolded,',
                'Grandiosely', 'Joyfully', 'Lazily', 'Angrily']

verbs = ['count', 'destroy', 'yeet', 'narrate', "don't touch", 'balance',
        'build with', 'sketch', 'photograph']

nouns = ['fruit', 'a chair', 'Spoons', 'spoons', 'a round object', 'paper products',
            'the ground', 'the air', 'some water', 'the first thing you see']

places = ['in the kitchen', 'balanced on a small surface', 'in the living room',
        'in the bedroom', 'in the basement', 'somewhere unexpected',
        'with no roof over your head', 'while horizontal', 'somewhere cold',
        'somewhere dark', 'somewhere warm', 'in the most open area']

# Generate activity
lists = [adjectives, verbs, nouns, places]
activity = ''
for list in lists:
    random_i = random.randint(0, len(list)-1)
    activity += list[random_i] + ' '

print(activity)

# Calculate total possible activities
n = 1
for list in lists:
    n = n*len(list)

print('This was randomly generated out of', n, 'possible activities.')
