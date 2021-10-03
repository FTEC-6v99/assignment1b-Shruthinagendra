# Use unittest library to create a unit test method to test the calc_avg_rating function created in the ratingscalc module
# Make sure you include multiple unit tests to test that the function acts as expected in different scenarios
import unittest

from app.src.Review import Review
from app.src.ratingscalc import calc_avg_rating


class TestRatingCalc(unittest.TestCase):

    # test for none reviews
    def testForNoneReviews(self):
        result = calc_avg_rating(None)
        self.assertEqual({}, result)

    # Test for
    def testForEmptyReviews(self):
        result = calc_avg_rating([])
        self.assertEqual({}, result)

    def testForAvgRatings(self):
        reviews = []

        reviews.append(Review('Red Cross', "Good ambience",
                       "I really enjoyed the food", 5))
        reviews.append(Review('Red Cross', "Average food",
                       "I dpn't really liked the food", 3))
        reviews.append(
            Review('Red Cross', "Nice and humle staff", "Staff was very good", 4))
        reviews.append(
            Review('My Ocean', "Wonderful and taste food", "I liked food", 4))
        reviews.append(Review('Garden Restaurant', "Very Clean",
                       "Restaurant was very clean", 5))
        reviews.append(Review('Garden Restaurant',
                       "Taste Food", "Food was very good", 4))
        reviews.append(Review('Garden Restaurant', "No parking",
                       "No Parking for customers", 2))

        result = calc_avg_rating(reviews)
        self.assertEqual(3.67, result['Garden Restaurant'])


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
