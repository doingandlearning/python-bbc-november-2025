from maths import add
import pytest

# Test driven development (TDD) 

# Happy path -> adds two numbers together
def test_two_whole_numbers_add_together_correctly():
  # Arrange - Given
  number1 = 10
  number2 = 20
  expected = 30
  
  # Act     - When
  result = add(number1, number2)  
  
  # Assert  - Then
  assert result == expected


# Edge cases -> decimals, negatives, big numbers, small numbers 
def test_two_decimals_add_correctly():
  assert add(0.1, 0.2) == pytest.approx(0.3)
  assert round(add(0.1, 0.2),1) == 0.3

@pytest.mark.parametrize('a, b, expected', [
    (0.01, 0.01, 0.02),
    (-100, -100, -200),
    (1_000_000, 1_000_000, 2_000_000),
    (3_000_000, 10, 3_000_010)
])
def test_happy_path_adding(a, b, expected):
  assert add(a, b) == expected

# Unhappy -> should raise if not numbers

def test_it_fails_when_adding_strings():
  with pytest.raises(TypeError):
    add("1", "2")