import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        for i in range(20):
            self.assertTrue(cart.add_dvd(DigitalVideoDisc(f"DVD {i}")))
        self.assertFalse(cart.add_dvd(DigitalVideoDisc("DVD 21")))

    def test_total_cost_with_discount(self):
        cart = Cart()
        # Thêm đĩa có tổng giá là 100.0$ để dễ tính toán
        cart.add_dvd(DigitalVideoDisc("Test DVD", cost=100.0))

        # 1. Kiểm tra tính đúng số tiền: giảm 20% của 100$ phải còn 80$
        self.assertAlmostEqual(cart.total_cost_with_discount(20), 80.0)

        # 2. Kiểm tra bắt lỗi khi phần trăm vượt quá 100% (ví dụ: 150%)
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)

if __name__ == "__main__":
    unittest.main()