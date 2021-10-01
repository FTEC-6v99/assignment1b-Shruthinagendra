# Create a unit test method to test the calculate_avg_rating function created in the utils module
# Make sure you include multiple unit tests to test that the function acts as expected in different scenarios
import unittest

from app.src.Review import Review
from app.src.utils import calculate_avg_rating


class TestUtils(unittest.TestCase):

    # test for none reviews
    def testForNoneReviews(self):
        result = calculate_avg_rating(None)
        self.assertEqual(0.0, result)

    # Test for
    def testForEmptyReviews(self):
        result = calculate_avg_rating([])
        self.assertEqual(0.0, result)

    def testForAvgRatings(self):
        reviews = []
        reviews.append(Review('Red Cross', "Good ambience",
                       "I really enjoyed the food", 5))
        reviews.append(
            Review('Red Cross', "Wonderful and taste food", "I liked food", 4))
        reviews.append(Review('Red Cross', "Very Clean",
                       "Restaurant was very clean", 5))
        result = calculate_avg_rating(reviews)
        self.assertEqual(4.67, result)

    def testForInvalidRatings(self):
        try:
            reviews = []
            reviews.append(Review('Red Cross', "Good ambience",
                           "I really enjoyed the food", 5))
            reviews.append(
                Review('Red Cross', "Wonderful and taste food", "I liked food", -4))
            reviews.append(Review('Red Cross', "Very Clean",
                           "Restaurant was very clean", 5))
            result = calculate_avg_rating(reviews)
            self.assertFalse("Test Failed!!!")
        except ValueError:
            self.assertTrue("Test Passed!!!")


# if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
   # unittest.main()
