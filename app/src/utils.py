# Create a function called calculate_avg_rating
# Parameters: the function should have one argument of type list of Review (i.e., the arg should be a list of Review objects)
# Returns: the function should return a float: the average of all raview ratings that are given in the list as an argument to this function.
#          The returned value should be rounded to the closest second decimal. Use the build-in round function: https://www.w3schools.com/python/ref_func_round.asp
#
# If the argument is an empty list, return 0.0
# for reference on exceptions, check the class notes here: https://github.com/FTEC-6v99/python-overview/blob/master/advanced/exceptions.py
#
# Make sure that you add type hints to the function paramter and return value

'''
Calculate the average of given reviews
reviews - List of reviews
return the rounded average of reviews
'''
# The average rating for restaurant review is created
import typing as t
from app.src.Review import Review


def calculate_avg_rating(reviews: t.List[Review]) -> float:
    total = 0.0
    if(reviews == None or len(reviews) == 0):
        return total
    for review in reviews:
        total += review.get_rating()
    if(len(reviews) > 0):
        total = total / len(reviews)
    return round(total, 2)
