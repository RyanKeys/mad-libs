import random


# Takes user input, and stores it in the respective array with variable prompt as function_name()


def user_input(function_name, array):
    recv_input = input(f"Enter some {function_name} seperated by spaces:")
    parsed_input = recv_input.split(" ")
    for i in parsed_input:
        array.append(i)
    print(array)
    return


# Place to store user input, and randomize
def adjectives():
    adj_dict = []
    user_input("adjectives", adj_dict)
    return random.choice(adj_dict)


def nouns():
    noun_dict = []
    user_input("nouns", noun_dict)
    return random.choice(noun_dict)


def verbs():
    verb_dict = []
    user_input("verbs", verb_dict)
    return random.choice(verb_dict)


# Inputs random list item into story based on int values assigned to functions
# Story from http://www.madlibs.com/printables/
adjectives = adjectives()
nouns = nouns()
verbs = verbs()


def story():
    return f'''A vacation is when you take a trip to some {adjectives} place
    with your {adjectives} family. Usually you go to some place
    that is near a/an {adjectives} or up on a/an {nouns}.
    A good vacation place is one where you can ride {nouns}
    or play {nouns} or go hunting for {nouns} . I like
    to spend my time {nouns} or {verbs}.
    When parents go on a vacation, they spend their time eating
    three {verbs} a day, and fathers play golf, and mothers
    sit around {nouns}. Last summer, my little brother
    fell in a/an {verbs} and got poison {verbs} all
    over his {verbs}. My family is going to go to (the)
    {verbs}, and I will practice {nouns}. Parents
    need vacations more than kids because parents are always very
    {adjectives} and because they have to work {adjectives}
    hours every day all year making enough {verbs} to pay
    for the vacation.'''


def test():
    print(story())


test()
