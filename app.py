import random

# Takes user input, and stores it in an array with variable prompt as function_name()


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
    random_adj = random.choice(adj_dict)
    return random_adj


def nouns():
    noun_dict = []
    user_input("nouns", noun_dict)
    return random.choice(noun_dict)


def verbs():
    verb_dict = []
    user_input("verbs", verb_dict)
    random_verb = random.choice(verb_dict)
    return random_verb


# Inputs random list item into story based on int values assigned to functions
# Story from http://www.madlibs.com/printables/

def story():
    return '''A vacation is when you take a trip to some {0} place
    with your {0} family. Usually you go to some place
    that is near a/an {0} or up on a/an {1}.
    A good vacation place is one where you can ride {1}
    or play {1} or go hunting for {1} . I like
    to spend my time {1} or {2}.
    When parents go on a vacation, they spend their time eating
    three {2} a day, and fathers play golf, and mothers
    sit around {1}. Last summer, my little brother
    fell in a/an {2} and got poison {2} all
    over his {2}. My family is going to go to (the)
    {2}, and I will practice {1}. Parents
    need vacations more than kids because parents are always very
    {0} and because they have to work {0}
    hours every day all year making enough {2} to pay
    for the vacation.'''.format(adjectives(), nouns(), verbs())


def test():
    print(story())


test()
