"""
Test the new convert function.

Note:
    Theses tests are the same tests defined in the other test modules.
"""
import unitconvert


def test_digitalunits():
    result = round(unitconvert.convert(326578, "MB", "TB"), 3)
    assert result == round(0.326578, 3), "Failed Test MB to TB"

    result = round(unitconvert.convert(26978, 'KiB', 'MB'), 3)
    assert result == round(27.625472, 3), "Failed Test KiB to MB"

    result = round(unitconvert.convert(5, 'GB', 'GiB'), 3)
    assert result == round(4.65661287308, 3), "Failed Test GB to GiB"

    # Test Exceptions
    try:
        unitconvert.convert(-32, 'MB', 'TB', error_on_negative=True)
        raise AssertionError("Failed to raise exception for negative MB to TB")
    except ValueError:
        pass

    try:
        unitconvert.convert(-2, 'KiB', 'MB', error_on_negative=True)
        raise AssertionError("Failed to raise exception for negative KiB to MB")
    except ValueError:
        pass

    try:
        unitconvert.convert(-6, 'GB', 'GiB', error_on_negative=True)
        raise AssertionError("Failed to raise exception for negative GB to GiB")
    except ValueError:
        pass


def test_lengthunits():
    result = round(unitconvert.convert(5.0, 'in', 'mm'), 2)
    assert result == round(127.0, 2), "Failed Test in to mm"

    result = round(unitconvert.convert(3.4, 'mi', 'km'), 2)
    assert result == round(5.47177, 2), "Failed Test mi to km"

    result = round(unitconvert.convert(2.5, 'ft', 'in'), 2)
    assert result == round(30.0, 2), "Failed Test mi to km"

    # Test if error on_negative works
    try:
        unitconvert.convert(-5.0, 'in', 'mm', error_on_negative=True)
        raise AssertionError("Failed to raise exception for negative in to mm")
    except ValueError:
        pass

    try:
        unitconvert.convert(-3.4, 'mi', 'km', error_on_negative=True)
        raise AssertionError("Failed to raise exception for negative mi to km")
    except ValueError:
        pass

    try:
        unitconvert.convert(-2.5, 'ft', 'in', error_on_negative=True)
        raise AssertionError("Failed to raise exception for negative ft to in")
    except ValueError:
        pass


def test_massunits():
    result = round(unitconvert.convert(16, 'oz', 'lb'), 2)
    assert result == round(1.0, 2), "Failed Test oz to lb"

    result = round(unitconvert.convert(27, 'g', 'lb'), 2)
    assert result == round(0.0595248107899, 2), "Failed Test g to lb"

    result = round(unitconvert.convert(1, 'oz', 'mg'), 2)
    assert result == round(28349.523125, 2), "Failed Test oz to mg"

    # Test if error on_negative works
    try:
        unitconvert.convert(-16, 'oz', 'lb', error_on_negative=True)
        raise AssertionError("Failed to raise exception for negative oz to lb")
    except ValueError:
        pass

    try:
        unitconvert.convert(-27, 'g', 'lb', error_on_negative=True)
        raise AssertionError("Failed to raise exception for negative g to lb")
    except ValueError:
        pass

    try:
        unitconvert.convert(-1, 'oz', 'mg', error_on_negative=True)
        raise AssertionError("Failed to raise exception for negative oz to mg")
    except ValueError:
        pass


def test_temperatureunits():
    result = round(unitconvert.convert(32, 'F', 'C'), 1)
    assert result == 0.0, "Failed Test F to C"

    result = round(unitconvert.convert(5, 'F', 'K'), 2)
    assert result == round(258.15, 2), "Failed Test F to K"

    result = round(unitconvert.convert(34, 'K', 'C'), 2)
    assert result == round(-239.15, 2), "Failed Test K to C"


def test_timeunits():
    result = round(unitconvert.convert(34, 'wk', 'yr'), 2)
    assert result == round(0.652055, 2), "Failed Test wk to yr"

    result = round(unitconvert.convert(1.7, 'hr', 'sec'), 2)
    assert result == round(6120.0, 2), "Failed Test hr to sec"

    result = round(unitconvert.convert(50, 'ms', 'min'), 4)
    assert result == round(0.000833333, 4), "Failed Test ms to min"

    # Test if error on_negative works
    try:
        unitconvert.convert(-34, 'wk', 'yr', error_on_negative=True)
        raise AssertionError("Failed to raise exception for negative wk to yr")
    except ValueError:
        pass

    try:
        unitconvert.convert(-1.7, 'hr', 'sec', error_on_negative=True)
        raise AssertionError("Failed to raise exception for negative hr to sec")
    except ValueError:
        pass

    try:
        unitconvert.convert(-50, 'ms', 'min', error_on_negative=True)
        raise AssertionError("Failed to raise exception for negative ms to min")
    except ValueError:
        pass


def test_volumeunits():
    result = round(unitconvert.convert(5.6, 'gal', 'in3'), 2)
    assert result == round(1293.6, 2), "Failed Test gal to in3"

    result = round(unitconvert.convert(56, 'ml', 'cup'), 2)
    assert result == round(0.236698, 2), "Failed Test ml to cup"

    result = round(unitconvert.convert(4.7, 'tbsp', 'l'), 4)
    assert result == round(0.0694978, 4), "Failed Test tbsp to l"

    result = round(unitconvert.convert(1, 'lcup', 'l'), 4)
    assert result == round(0.24, 4), "Failed Test lcup to l"

    result = round(unitconvert.convert(1, 'cup', 'floz'), 4)
    assert result == round(8.0, 4), "Failed Test cup to floz"

    # Test if error on_negative works
    try:
        unitconvert.convert(-4, 'gal', 'in3', error_on_negative=True)
        raise AssertionError("Failed to raise exception for negative gal to in3")
    except ValueError:
        pass

    try:
        unitconvert.convert(-5, 'ml', 'cup', error_on_negative=True)
        raise AssertionError("Failed to raise exception for negative ml to cup")
    except ValueError:
        pass

    try:
        unitconvert.convert(-8, 'tbsp', 'l', error_on_negative=True)
        raise AssertionError("Failed to raise exception for negative tbsp to l")
    except ValueError:
        pass


if __name__ == '__main__':
    test_digitalunits()
    test_lengthunits()
    test_massunits()
    test_temperatureunits()
    test_timeunits()
    test_volumeunits()
    print("All tests passed successfully!")
