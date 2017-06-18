#!/usr/bin/env python
# -*- coding: utf8 -*-

from __future__ import division
from numpy import sqrt


class Star:
    """
    Class to create objects related stars
    author: D. Andreasen
    """
    grav = 6.67384e-11  # Gravitational constant
    au = 149597871  # average distance to the Sun from Earth

    def __init__(self, massin, radiusin):
        self.mass = massin
        self.radius = radiusin

    def get_surface_gravity(self):
        return Star.grav * self.mass / self.radius ** 2

    def __str__(self):
        # Fancy printing of a star
        string = ''
        string += '\n' + '*' * 33 + '\n'
        string += '*** Welcome to the Star class ***\n'
        string += '*' * 33 + '\n'
        string += 'Mass is\t\t\t %.2f\n' % self.mass
        string += 'Radius is\t\t %.2f\n' % self.radius
        string += 'Surface gravity is\t %s\n' % self.get_surface_gravity()
        return string

    def __add__(self, other):
        return Star(self.mass + other.mass, sqrt(self.radius + other.radius))

    @staticmethod
    def get_spectral_types():
        return ['O', 'B', 'A', 'F', 'G', 'K', 'M']


def main():

    # Create two stars
    star1 = Star(1.1, 0.98)
    star2 = Star(0.8, 1.3)

    # Try to print them
    print star1
    print star2

    # Now print the sum of the two stars
    print star1 + star2


if __name__ == '__main__':
    main()
