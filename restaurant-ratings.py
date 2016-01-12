# your code goes here
import sys

def print_alphabetical_ratings(filepath):
    ratings_file = open(filepath)
    restaurant_ratings = {}

    for line in ratings_file:
        restaurant, rating = line.rstrip().split(':')
        restaurant_ratings[restaurant] = rating

    sorted_restaurants = sorted(restaurant_ratings.keys())

    for restaurant in sorted_restaurants:
        print "{} is rated at {}.".format(restaurant, restaurant_ratings[restaurant])

    ratings_file.close()

print_alphabetical_ratings(sys.argv[1])
