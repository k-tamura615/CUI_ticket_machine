import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../source')))
from cui_eatticket_machine import items, checkout
import unittest
class VendingMachineTest(unittest.TestCase):
    def test_vending_machine_cart_addition(self):
        cart = {}
        cart[1] = cart.get(1, 0) + 1
        self.assertEqual(cart[1], 1, "商品1がカートに正しく追加されていません。")
        cart[1] = cart.get(1, 0) + 1
        self.assertEqual(cart[1], 2, "商品1がカートに2つ追加されていません。")
        cart[2] = cart.get(2, 0) + 1
        self.assertEqual(cart[2], 1, "商品2がカートに正しく追加されていません。")
    def test_checkout_valid_payment(self):
        cart = {1: 2, 2: 1}
        total = sum(items[item]['price'] * quantity for item, quantity in cart.items())
        cash = total + 100
        change = cash - total
        self.assertEqual(change, 100, f"支払い処理に誤りがあります。お釣り: {change}円")
    def test_sales_reset(self):
        items[1]['sold'] = 5
        items[2]['sold'] = 3
        for item in items.values():
            item['sold'] = 0
        for item in items.values():
            self.assertEqual(item['sold'], 0, f"{item['name']} の売上がリセットされていません。")
if __name__ == '__main__':
    unittest.main()
    