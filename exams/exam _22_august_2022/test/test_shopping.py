from project.shopping_cart import ShoppingCart
import unittest


class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.shopping_cart = ShoppingCart("Shop", 25000.20)

    def test_init(self):
        self.assertEqual(self.shopping_cart.shop_name, 'Shop')
        self.assertEqual(self.shopping_cart.budget, 25000.20)
        self.assertEqual(self.shopping_cart.products, {})

    def test_if_name_is_invalid(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart = ShoppingCart("shop", 12331)
        self.assertEqual(str(ve.exception), "Shop must contain only letters and must start with capital letter!")

        with self.assertRaises(ValueError) as ve:
            self.shopping_cart = ShoppingCart('Shop123', 412421)
        self.assertEqual(str(ve.exception), "Shop must contain only letters and must start with capital letter!")

    def test_add_to_cart_if_product_price_is_greater_or_equal_100(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.add_to_cart("Laptop", 1500)
        self.assertEqual(str(ve.exception), "Product Laptop cost too much!")

    def test_add_to_cart(self):
        result = self.shopping_cart.add_to_cart('Tablet', 55.23)
        expected_result = "Tablet product was successfully added to the cart!"
        self.assertEqual(result, expected_result)
        self.assertEqual(self.shopping_cart.products, {"Tablet": 55.23})

    def test_remove_from_cart_if_product_not_in_products(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.remove_from_cart('Product')
        self.assertEqual(str(ve.exception), "No product with name Product in the cart!")

    def test_remove_from_cart(self):
        self.shopping_cart.add_to_cart("Product", 26.20)
        self.shopping_cart.add_to_cart("Second Product", 22.20)
        result = self.shopping_cart.remove_from_cart("Product")
        expected_result = "Product Product was successfully removed from the cart!"
        self.assertEqual(result, expected_result)
        self.assertEqual(self.shopping_cart.products, {"Second Product": 22.20})

    def test_add_method(self):
        self.shopping_cart.add_to_cart("Product", 20)
        other_product = ShoppingCart("Name", 22000.50)
        other_product.add_to_cart("Second Product", 25)
        result = self.shopping_cart.__add__(other_product)
        self.assertEqual(result.shop_name, "ShopName")
        self.assertEqual(result.budget, 47000.70)
        self.assertEqual(result.products, {"Product": 20, "Second Product": 25})

    def test_buy_products_if_total_sum_is_greater_budget(self):
        self.shopping_cart = ShoppingCart("Shop", 20)
        self.shopping_cart.add_to_cart("Product", 50)
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.buy_products()
        self.assertEqual(str(ve.exception), "Not enough money to buy the products! Over budget with 30.00lv!")

    def test_buy_products(self):
        self.shopping_cart.add_to_cart("Product", 20)
        self.shopping_cart.add_to_cart("Other Product", 25.25)
        result = self.shopping_cart.buy_products()
        expected_result = 'Products were successfully bought! Total cost: 45.25lv.'
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()

