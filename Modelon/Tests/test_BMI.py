import sys
import os

# Add the parent directory of Tests to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from Classes_Folder.BMI_Class import BMICalculator

def test_bmi_calculation_valid_input():
    calculator = BMICalculator()
    weight = 60.0
    height = 1.75
    expected_bmi = 19.59
    assert calculator.calculate_bmi(weight, height) == pytest.approx(expected_bmi, abs=0.01)

def test_bmi_category_underweight_severe():
    calculator = BMICalculator()
    bmi = 15.0
    expected_category = "Underweight (Severe thinness)"
    assert calculator.get_bmi_category(bmi) == expected_category

def test_bmi_category_normal_range():
    calculator = BMICalculator()
    bmi = 22.0
    expected_category = "Normal range"
    assert calculator.get_bmi_category(bmi) == expected_category

def test_bmi_category_obese_class_iii():
    calculator = BMICalculator()
    bmi = 45.0
    expected_category = "Obese (Class III)"
    assert calculator.get_bmi_category(bmi) == expected_category

def test_bmi_calculation_invalid_input():
    calculator = BMICalculator()
    
    # Test with negative weight (invalid input)
    weight = -50.0
    height = 1.75
    
    # Use pytest.raises context manager to check for expected ValueError
    with pytest.raises(ValueError):
        calculator.calculate_bmi(weight, height)

    # Test with zero height (invalid input)
    weight = 60.0
    height = 0.0
    
    # Use pytest.raises context manager to check for expected ValueError
    with pytest.raises(ValueError):
        calculator.calculate_bmi(weight, height)
