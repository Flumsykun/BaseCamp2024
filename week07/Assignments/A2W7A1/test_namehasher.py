import unittest
from namehasher import encode_string, decode_string, set_dict_key, DEFAULT_KEY, dict_key_value, decode_list, \
    encode_list, validate_values


class TestNameHasher(unittest.TestCase):

    def setUp(self):
        """Set up the test environment."""
        # Set the default key for testing
        set_dict_key(DEFAULT_KEY)

    def test_set_dict_key(self):
        """Test if the dictionary key is set correctly."""
        key = "ABCD"
        set_dict_key(key)
        # Check that dictionary is correctly set
        self.assertEqual(dict_key_value, {'A': 'B', 'C': 'D'})

        # Test if key length is even
        with self.assertRaises(ValueError):
            set_dict_key("A")  # Invalid key length (should raise ValueError)

    def test_encode_string(self):
        """Test encoding a string."""
        value = "PETER"
        encoded = encode_string(value)
        self.assertEqual(encoded, 'P#T#R')

        value_with_special_chars = "A%B&C(D)"
        encoded_special = encode_string(value_with_special_chars)
        self.assertEqual(encoded_special, '>*;*#')

    def test_decode_string(self):
        """Test decoding a string."""
        encoded = 'P#T#R'
        decoded = decode_string(encoded)
        self.assertEqual(decoded, 'PETER')

        encoded_special = '>*;*#'
        decoded_special = decode_string(encoded_special)
        self.assertEqual(decoded_special, 'A%B&C(D)')

    def test_encode_list(self):
        """Test encoding a list of strings."""
        values = ["PETER", "PAN"]
        encoded_list = encode_list(values)
        self.assertEqual(encoded_list, ['P#T#R', 'P*N'])

    def test_decode_list(self):
        """Test decoding a list of strings."""
        encoded_values = ['P#T#R', 'P*N']
        decoded_list = decode_list(encoded_values)
        self.assertEqual(decoded_list, ['PETER', 'PAN'])

    def test_invalid_encode_input(self):
        """Test invalid encoding input."""
        with self.assertRaises(KeyError):
            encode_string("INVALID_CHAR")

    def test_invalid_decode_input(self):
        """Test invalid decoding input."""
        with self.assertRaises(KeyError):
            decode_string("INVALID_CHAR")

    def test_validate_values(self):
        """Test if validation works for matching encoded/decoded values."""
        encoded = 'P#T#R'
        decoded = 'PETER'
        self.assertTrue(validate_values(encoded, decoded))

        invalid_encoded = 'P#T#R'
        invalid_decoded = 'PETERX'
        self.assertFalse(validate_values(invalid_encoded, invalid_decoded))

    def test_invalid_choice(self):
        """Test invalid menu choice."""
        invalid_choice = "X"
        with self.assertRaises(ValueError):
            if invalid_choice not in ['E', 'D', 'P', 'V', 'Q']:
                raise ValueError("Invalid choice. Please try again.")


if __name__ == '__main__':
    unittest.main()
