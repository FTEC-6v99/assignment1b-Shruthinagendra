# Create a function called: calc_avg_rating
# Parameters: the function should receive 1 parameter: a list of review objects
#             Remember a list can contain duplicates, so you can expect multiple reviews for the same restaurant
# Returns: the function should return a dictionary with restaurant name as key and average rating as value
#
#
# If the list of reviews is empty, return an empty dictionary
# Make sure that you add type hints to the function paramter and return value

'''
reviews - List pf reviews
Return Dictionary for restaurant name and it's aveg
'''
import typing as t
from app.src.Review import Review
from app.src.utils import calculate_avg_rating


def calc_avg_rating(reviews: t.List[Review]) -> t.Mapping[str, float]:
    if(None == reviews or len(reviews) == 0):
        return {}
    restaurantRatings = {}
    restaurantRatingCount = {}

    for review in reviews:
        if(review.get_restaurant() in restaurantRatings.keys()):
            restaurantRatings[review.get_restaurant()] += review.get_rating()
            restaurantRatingCount[review.get_restaurant()] += 1
        else:
            restaurantRatings[review.get_restaurant()] = review.get_rating()
            restaurantRatingCount[review.get_restaurant()] = 1
    for restaurant in restaurantRatings.keys():
        restaurantRatings[restaurant] = round(
            restaurantRatings[restaurant] / restaurantRatingCount[restaurant], 2)
    return restaurantRatings
