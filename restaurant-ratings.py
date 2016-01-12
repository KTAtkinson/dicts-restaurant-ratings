import random
import sys

def get_ratings(filepath):
    ratings_file = open(filepath)
    restaurant_ratings = {}

    for line in ratings_file:
        restaurant, rating = line.rstrip().split(':')
        restaurant_ratings[restaurant] = rating

    ratings_file.close()

    return restaurant_ratings


def print_alphabetical_ratings(ratings):
    """Print ratings alphabetically from a dictionary"""

    sorted_restaurants = sorted(ratings.keys())

    for restaurant in sorted_restaurants:
        print "{} is rated at {}.".format(restaurant, ratings[restaurant])


def add_rating(ratings):
    restaurant_name = raw_input('Enter restaurant name: ')
    restaurant_score = raw_input('Enter a score for {}: '.format(restaurant_name))
    restaurant_score = get_int_from_user(restaurant_score)
    if not restaurant_score:
        return

    ratings[restaurant_name] = restaurant_score

    print_alphabetical_ratings(ratings)


def update_ratings(ratings):
    user_name = raw_input('Hello, what\'s your name?: ')
    print "Hi {}, nice to meet you! If you'd like to quit at any time, please press 'q'.".format(user_name)

    updating = True
    while updating:
        random_restaurant = random.choice(ratings.keys())
        print "We chose {}, which has a rating of {}.".format(random_restaurant, ratings[random_restaurant])
        new_rating = raw_input("Please enter a new rating for {}: ".format(random_restaurant))
        new_rating = get_int_from_user(new_rating)
        if not new_rating:
            updating = False
        ratings[random_restaurant] = new_rating

    print_alphabetical_ratings(ratings)


def get_int_from_user(user_input):
    while not user_input.isdigit():
        if user_input == "q":
            return None
        user_input = raw_input("That's not a number! Please enter a number again: ")
    

    return int(user_input)

data = get_ratings(sys.argv[1])
print 'Enter "p" to print, "a" to add, "u" to update, or "q" to quit.'

running = True
while running:
    user_choice = raw_input('What would you like to do? ')

    if user_choice == 'p':
        print_alphabetical_ratings(data)
    elif user_choice == 'a':
        add_rating(data)
    elif user_choice == 'u':
        update_ratings(data)
    elif user_choice == 'q':
        running = False
    else:
        print 'That is not a valid input. Enter "p" to print, "a" to add, "u" to update, or "q" to quit'


