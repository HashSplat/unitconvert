"""placeholder docstring"""

class DigitalUnit(object):
    """placeholder docstring"""
    def __init__(self):
        self.decimal_base = 1.0
        self.binary_base = 1.024

    def getunitval(self, argument):
        """Takes a unit and returns a function to calculate the unit's value"""
        function = 'unit_{0}'.format(str(argument))
        function = getattr(self, function, lambda: None)
        return function()

    def unit_B(self):
        """placeholder docstring"""
        return self.decimal_base

    def unit_kB(self):
        """placeholder docstring"""
        return self.decimal_base * 1000

    def unit_MB(self):
        """placeholder docstring"""
        return (self.decimal_base * 1000) ** 2

    def unit_GB(self):
        """placeholder docstring"""
        return (self.decimal_base * 1000) ** 3

    def unit_TB(self):
        """placeholder docstring"""
        return (self.decimal_base * 1000) ** 4

    def unit_PB(self):
        """placeholder docstring"""
        return (self.decimal_base * 1000) ** 5

    def unit_EB(self):
        """placeholder docstring"""
        return (self.decimal_base * 1000) ** 6

    def unit_ZB(self):
        """placeholder docstring"""
        return (self.decimal_base * 1000) ** 7

    def unit_YB(self):
        """placeholder docstring"""
        return (self.decimal_base * 1000) ** 8