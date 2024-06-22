# tests/test_complex_numbers.py
import pytest
from Calculator.Source_Code import complex_numbers


def test_add_complex():
    assert complex_numbers.add_complex(1, 2, 3, 4) == (4, 6)

def test_multiply_complex():
    assert complex_numbers.multiply_complex(1, 2, 3, 4) == (-5, 10)

# tests/test_basic_calculator.py

from Calculator.Source_Code import calculate as calculate_basic

def test_calculate_basic_addition():
    assert calculate_basic('2 + 3') == '5'

def test_calculate_basic_subtraction():
    assert calculate_basic('5 - 3') == '2'

# tests/test_matrix_operations.py

from Calculator.Source_Code.matrix_operations import calculate as calculate_matrix

def test_calculate_matrix_addition():
    # Define input matrices
    matrix1 = [[1, 1], [1, 1]]
    matrix2 = [[1, 1], [1, 1]]

    # Call calculate_matrix with 'multiply' operation and matrices
    result = calculate_matrix('add', [matrix1, matrix2])

    # Assert the result matches the expected output
    assert result == [[2, 2], [2, 2]]


# Define a test function for matrix multiplication
def test_calculate_matrix_multiplication():
    # Define input matrices
    matrix1 = [[1, 1], [1, 1]]
    matrix2 = [[1, 1], [1, 1]]

    # Call calculate_matrix with 'multiply' operation and matrices
    result = calculate_matrix('multiply', [matrix1, matrix2])

    # Assert the result matches the expected output
    assert result == [[2, 2], [2, 2]]
# tests/test_symbolic_computation.py

from Calculator.Source_Code import differentiate, integrate_expression


def test_differentiate():
    assert differentiate('x**2', 'x') == '2*x'

def test_integrate_expression():
    assert integrate_expression('x**2') == 'x**3/3'

# tests/test_unit_conversion.py

from Calculator.Source_Code import convert_units

def test_convert_units_length():
    data = {'from_unit': 'meters', 'to_unit': 'feet', 'value': '10'}
    assert convert_units(data) == pytest.approx(32.8084, rel=1e-4)

def test_convert_units_temperature():
    data = {'from_unit': 'celsius', 'to_unit': 'fahrenheit', 'value': '100'}
    assert convert_units(data) == pytest.approx(212.0, rel=1e-4)




