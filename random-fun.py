import random

adjectives = ['Quickly', 'Seriously', 'Slowly', 'With fear,', 'Blindfolded,',
                'Grandiosely', 'Joyfully', 'Lazily', 'Angrily']
random_adj = random.randint(0,len(adjectives)-1)

verbs = ['count', 'destroy', 'yeet', 'narrate', "don't touch", 'balance',
        'build with', 'sketch', 'photograph']
random_verb = random.randint(0,len(verbs)-1)

nouns = ['fruit', 'a chair', 'Spoons', 'spoons', 'a round object', 'paper products',
            'the ground', 'the air', 'some water', 'the first thing you see']
random_noun = random.randint(0, len(nouns)-1)

places = ['in the kitchen', 'balanced on a small surface', 'in the living room',
        'in the bedroom', 'in the basement', 'somewhere unexpected',
        'with no roof over your head', 'while horizontal', 'somewhere cold',
        'somewhere dark', 'somewhere warm', 'in the most open area']
random_place = random.randint(0, len(places)-1)

print(adjectives[random_adj], verbs[random_verb], nouns[random_noun], places[random_place])

n = 1
lists = [adjectives, verbs, nouns, places]
for list in lists:
    n = n*len(list)

print('This was randomly generated out of', n, 'possible activities.')
