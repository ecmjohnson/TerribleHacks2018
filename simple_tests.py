from types import FunctionType
import random

def test_1(compiled_code, similarity_metric):

		expected = 14

		result = compiled_code(8, 6)
		err    = similarity_metric(expected, result)

		return (result == expected, err)

def test_2(compiled_code, similarity_metric):

		expected = 15

		result = compiled_code(7, 8)
		err    = similarity_metric(expected, result)

		return (result == expected, err)

def test_3(compiled_code, similarity_metric):

		expected = 7

		result = compiled_code(4, 3)
		err    = similarity_metric(expected, result)

		return (result == expected, err)

class Simple_Tests:

    test_1 = test_1
    test_2 = test_2
    test_3 = test_3