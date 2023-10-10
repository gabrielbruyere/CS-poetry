from cs_poetry import functions
import unittest

class Test_Functions(unittest.TestCase):

    def test_nearest_value(self):
        values = {4, 7, 10, 11, 12, 17}
        self.assertEqual(functions.nearest_value(values, 9), 10)
        self.assertEqual(functions.nearest_value(values, 8), 7)
        self.assertEqual(functions.nearest_value(values, 0), 4)

    def test_first_word(self):
        self.assertEqual(functions.first_word("Hello World"), "Hello")
        self.assertEqual(functions.first_word("   Leading spaces"), "Leading")
        self.assertEqual(functions.first_word(""), "")
        
    def test_split_pairs(self):
        self.assertEqual(list(functions.split_pairs("abcd")), ["ab", "cd"])
        self.assertEqual(list(functions.split_pairs("abc")), ["ab", "c_"])
        self.assertEqual(list(functions.split_pairs("abcdf")), ["ab", "cd", "f_"])

    def test_correct_sentence(self):
        self.assertEqual(functions.correct_sentence("hello"), "Hello.")
        self.assertEqual(functions.correct_sentence("greetings, friends"), "Greetings, friends.")
        self.assertEqual(functions.correct_sentence("greetings, friends."), "Greetings, friends.")
        self.assertEqual(functions.correct_sentence("Greetings, friends"), "Greetings, friends.")

    def test_beginning_zeros(self):
        self.assertEqual(functions.beginning_zeros("100"), 0)
        self.assertEqual(functions.beginning_zeros("001"), 2)
        self.assertEqual(functions.beginning_zeros("100100"), 0)
        self.assertEqual(functions.beginning_zeros("001001"), 2)

    def test_between_markers(self):
        self.assertEqual(functions.between_markers("What is >apple<", ">", "<"), "apple")
        self.assertEqual(functions.between_markers("What is [apple]", "[", "]"), "apple")
        self.assertEqual(functions.between_markers("What is ><", ">", "<"), "")
        self.assertEqual(functions.between_markers("[an apple]", "[", "]"), "an apple")

    def test_checkio(self):
        self.assertEqual(list(functions.checkio([1, 2, 3, 1, 3])), [1, 3, 1, 3])
        self.assertEqual(list(functions.checkio([1, 2, 3, 4, 5])), [])
        self.assertEqual(list(functions.checkio([5, 5, 5, 5, 5])), [5, 5, 5, 5, 5])
        self.assertEqual(list(functions.checkio([10, 9, 10, 10, 9, 8])), [10, 9, 10, 10, 9])

    def test_backward_string_by_word(self):
        self.assertEqual(functions.backward_string_by_word("Hello World"), "olleH dlroW")
        self.assertEqual(functions.backward_string_by_word("  Leading spaces"), "  gnidaeL secaps")

if __name__ == '__main__':
    unittest.main()