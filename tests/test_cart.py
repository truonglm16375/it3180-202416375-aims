import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc

class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        for i in range(20):
            self.assertTrue(cart.add_dvd(DigitalVideoDisc(f"DVD {i}")))
        self.assertFalse(cart.add_dvd(DigitalVideoDisc("DVD 21")))

    def test_total_cost_with_discount_valid(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("Test DVD", cost=100.0))
        self.assertAlmostEqual(cart.total_cost_with_discount(20), 80.0)

    def test_total_cost_with_discount_invalid_percent(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("Test DVD", cost=100.0))
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)

    def test_sort_by_title(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("Star Wars", cost=20.0))
        cart.add_dvd(DigitalVideoDisc("Aladdin", cost=15.0))
        cart.add_dvd(DigitalVideoDisc("The Lion King", cost=10.0))

        cart.sort_by_title()
        titles = [dvd.title for dvd in cart.items]
        self.assertEqual(titles, ["Aladdin", "Star Wars", "The Lion King"])

    def test_sort_by_cost(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("Star Wars", cost=20.0))
        cart.add_dvd(DigitalVideoDisc("Aladdin", cost=15.0))
        cart.add_dvd(DigitalVideoDisc("The Lion King", cost=25.0))

        cart.sort_by_cost()
        costs = [dvd.cost for dvd in cart.items]
        self.assertEqual(costs, [25.0, 20.0, 15.0])

if __name__ == "__main__":
    unittest.main()