import importlib.util
import pytest

spec = importlib.util.spec_from_file_location("grade_calculator", "grade-calculator.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

average = mod.average
grade = mod.grade
is_pass = mod.is_pass

def test_average():
    assert average([80, 90, 100]) == 90
    assert average([50, 50]) == 50

def test_average_empty():
    with pytest.raises(ValueError):
        average([])

def test_grade():
    assert grade(95) == "A+"
    assert grade(85) == "A"
    assert grade(75) == "B"
    assert grade(65) == "C"
    assert grade(55) == "D"
    assert grade(30) == "F"

def test_is_pass():
    assert is_pass([50, 60, 70]) == True
    assert is_pass([30, 60, 70]) == False
