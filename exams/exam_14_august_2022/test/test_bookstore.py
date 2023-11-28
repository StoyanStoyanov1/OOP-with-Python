from project.bookstore import Bookstore
import unittest


class TestBookStore(unittest.TestCase):

    def setUp(self):
        self.book_store = Bookstore(10)

    def test_init(self):
        self.assertEqual(self.book_store.books_limit, 10)
        self.assertEqual(self.book_store.availability_in_store_by_book_titles, {})
        self.assertEqual(self.book_store.total_sold_books, 0)

    def test_books_limit_if_limit_is_not_greater_0(self):
        with self.assertRaises(ValueError) as ve:
            self.book_store = Bookstore(0)
        self.assertEqual(str(ve.exception), "Books limit of 0 is not valid")

    def test_len_method(self):
        self.book_store.availability_in_store_by_book_titles = {'book': 4, 'other_book': 7}
        result = self.book_store.__len__()
        self.assertEqual(result, 11)

    def test_receive_book_exception_error(self):
        self.book_store.availability_in_store_by_book_titles = {'book': 4, 'other_book': 7}
        with self.assertRaises(Exception) as ex:
            self.book_store.receive_book("other_book", 2)
        self.assertEqual(str(ex.exception), "Books limit is reached. Cannot receive more books!")

    def test_receive_book(self):
        self.book_store.availability_in_store_by_book_titles = {'book': 1, 'other_book': 3}
        result = self.book_store.receive_book("three_book", 1)
        expected_result = "1 copies of three_book are available in the bookstore."
        self.assertEqual(result, expected_result)
        self.assertEqual(self.book_store.availability_in_store_by_book_titles,
                         {'book': 1, 'other_book': 3, "three_book": 1})
        result = self.book_store.receive_book("three_book", 2)
        expected_result = "3 copies of three_book are available in the bookstore."
        self.assertEqual(result, expected_result)
        self.assertEqual(self.book_store.availability_in_store_by_book_titles,
                         {'book': 1, 'other_book': 3, "three_book": 3})

    def test_sell_book_by_invalid_title(self):
        with self.assertRaises(Exception) as ex:
            self.book_store.sell_book('title', 2)

        self.assertEqual(str(ex.exception), "Book title doesn't exist!")

    def test_sell_book_if_not_enough_copies(self):
        self.book_store.availability_in_store_by_book_titles = {'book': 1, 'other_book': 3}
        with self.assertRaises(Exception) as ex:
            self.book_store.sell_book('book', 2)
        self.assertEqual(str(ex.exception), "book has not enough copies to sell. Left: 1")

    def test_sell_book(self):
        self.book_store.availability_in_store_by_book_titles = {'book': 1, 'other_book': 3}
        result = self.book_store.sell_book("other_book", 2)
        expected_result = "Sold 2 copies of other_book"

        self.assertEqual(result, expected_result)
        self.assertEqual(self.book_store.availability_in_store_by_book_titles, {'book': 1, 'other_book': 1})
        self.assertEqual(self.book_store.total_sold_books, 2)

        result = self.book_store.sell_book("other_book", 1)
        expected_result = "Sold 1 copies of other_book"
        self.assertEqual(result, expected_result)
        self.assertEqual(self.book_store.availability_in_store_by_book_titles, {'book': 1, 'other_book': 0})
        self.assertEqual(self.book_store.total_sold_books, 3)

    def test_str(self):
        self.book_store.availability_in_store_by_book_titles = {'book': 1, 'other_book': 3}
        result = str(self.book_store)
        expected_result = "Total sold books: 0\nCurrent availability: 4\n - book: 1 copies\n - other_book: 3 copies"
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
