#!/usr/bin/env python3
"""
The Mystical Dragon - Mastering Mixins
"""


class SwimMixin:
    """
    Mixin class that provides swimming capability
    """
    
    def swim(self):
        """
        Print swimming message
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin class that provides flying capability
    """
    
    def fly(self):
        """
        Print flying message
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class that inherits swimming and flying capabilities from mixins
    """
    
    def roar(self):
        """
        Dragon's unique ability to roar
        """
        print("The dragon roars!")
