# create a new class called Review
# the class must have the following properties/attributes:
# 1. restaurant: name of the restaurant
# 2. review_title: the title of the review
# 3. review_body: the body of the review
# 4. rating: a numeric rating from 1 to 5
#
# Your class constructor (init function) must raise an Exception if
# rating provided was not between 1 and 5
#
# Use typing module to hint the class attributes


class Review(object):

    def __init__(self, restaurant: str, review_title: str, review_body: str, rating: int):
        if(rating < 1 or rating > 5):
            raise ValueError("Invalid value for rating!!!")
        self.restaurant = restaurant
        self.review_title = review_title
        self.review_body = review_body
        self.rating = rating

    def get_restaurant(self):
        return self.restaurant

    def get_review_title(self):
        return self.review_title

    def get_review_body(self):
        return self.review_body

    def get_rating(self):
        return self.rating

    def set_restaurant(self, value):
        self.restaurant = value

    def set_review_title(self, value):
        self.review_title = value

    def set_review_body(self, value):
        self.review_body = value

    def set_rating(self, value):
        self.rating = value
