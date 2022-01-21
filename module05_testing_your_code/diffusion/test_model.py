from .model import energy
from pytest import raises

def test_energy_empty_array():
    """Optional description for nose reporting."""
    # Test something
    with raises(TypeError) as exception:
        energy([])
    
   
def test_energy_non_integer():
    """Optional description for nose reporting."""
    # Test something
    with raises(TypeError) as exception:
        energy([1.5, 3])

def test_energy_negative_values():
    """Optional description for nose reporting."""
    # Test something
    with raises(ValueError) as exception:
        energy([1, -2, -3])

def test_energy_1D_array():
    """Optional description for nose reporting."""
    # Test something
    with raises(TypeError) as exception:
        assert energy([[1, 3], [2,2]])

def test_energy_zero_energy():
    """Optional description for nose reporting."""
    # Test something
    with raises(ValueError) as exception:
        energy([0,0,0,0,0]) != 0