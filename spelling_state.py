
from itertools import product
from ntpath import join
import us
import string


def spelling_state():
    states = [str(st).lower().replace(" ", "") for st in us.STATES]
    vowels = "aeiou"
    consonents = string.ascii_lowercase

    for v in vowels:
        consonents = consonents.replace(v, "")
    #print(vowels, consonents)

    for consonent, vowel in product(consonents, vowels):
        found = 0
        missing_states = []
        #print(consonent, vowel)
        for state in states:
            if consonent in state or vowel in state:
                found += 1
            else:
                missing_states.append(state)

            if found == 47:
                print("Consonent: ", consonent)
                print("Vowel: ", vowel)
                print("Missing States:", missing_states)


spelling_state()
