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

if __name__ == "__main__":
    unittest.main()