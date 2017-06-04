# pylint: disable=I0011,C0103

"""placeholder docstring"""


class DigitalUnit(object):
    """placeholder docstring"""
    def __init__(self):
        #self.powers_def = powers_def
        self.decimal_base = 1.0  # bytes in a byte (decimal)
        self.binary_base = 1.024 # bytes in a byte (binary)

    def getunitval(self, argument):
        """Return a function to calculate the unit's value"""
        function = 'unit_{0}'.format(str(argument))
        function = getattr(self, function, lambda: None)
        return function()

    def unit_B(self):
        """Return the value of one Byte (B)
        based on a base decimal value"""
        return self.decimal_base

    def unit_kB(self):
        """Return the value of one Kilobyte (kB)
        based on a base decimal value"""
        return self.decimal_base * 1000

    def unit_KiB(self):
        """Return the value of one Kibibyte (KiB)
        based on a base binary value"""
        return self.binary_base * 1000

    def unit_MB(self):
        """Return the value of one Megabyte (MB)
        based on a base decimal value"""
        return (self.decimal_base * 1000) ** 2

    def unit_MiB(self):
        """Return the value of one Mebibyte (MiB)
        based on a base binary value"""
        return (self.binary_base * 1000) ** 2

    def unit_GB(self):
        """Return the value of one Gigabyte (GB)
        based on a base decimal value"""
        return (self.decimal_base * 1000) ** 3

    def unit_GiB(self):
        """Return the value of one Gibibyte (GiB)
        based on a base binary value"""
        return (self.binary_base * 1000) ** 3

    def unit_TB(self):
        """Return the value of one Terabyte (TB)
        based on a base decimal value"""
        return (self.decimal_base * 1000) ** 4

    def unit_TiB(self):
        """Return the value of one Tebibyte (TiB)
        based on a base binary value"""
        return (self.binary_base * 1000) ** 4

    def unit_PB(self):
        """Return the value of one Petabyte (PB)
        based on a base decimal value"""
        return (self.decimal_base * 1000) ** 5

    def unit_PiB(self):
        """Return the value of one Pebibyte (PiB)
        based on a base binary value"""
        return (self.binary_base * 1000) ** 5

    def unit_EB(self):
        """Return the value of one Exabyte (EB)
        based on a base decimal value"""
        return (self.decimal_base * 1000) ** 6

    def unit_EiB(self):
        """Return the value of one Exbibyte (EiB)
        based on a base binary value"""
        return (self.binary_base * 1000) ** 6

    def unit_ZB(self):
        """Return the value of one Zettabyte (ZB)
        based on a base decimal value"""
        return (self.decimal_base * 1000) ** 7

    def unit_ZiB(self):
        """Return the value of one Zebibyte (ZiB)
        based on a base binary value"""
        return (self.binary_base * 1000) ** 7

    def unit_YB(self):
        """Return the value of one Yottabyte (YB)
        based on a base decimal value"""
        return (self.decimal_base * 1000) ** 8

    def unit_YiB(self):
        """Return the value of one Yobibyte (YiB)
        based on a base binary value"""
        return (self.binary_base * 1000) ** 8
