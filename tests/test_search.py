import unittest
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title

class TestSearch(unittest.TestCase):
    def test_search_by_title_found(self):
        dvds = [
            DigitalVideoDisc("The Lion King"),
            DigitalVideoDisc("Star Wars"),
            DigitalVideoDisc("Aladdin")
        ]
        results = search_by_title(dvds, "Star")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Star Wars")

if __name__ == "__main__":
    unittest.main()