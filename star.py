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

    def __init__(self, massin, radiusin):
        self.mass = massin
        self.radius = radiusin

    def get_surface_gravity(self):
        return Star.grav * self.mass / self.radius ** 2

    @staticmethod
    def get_spectral_types():
        return ['O', 'B', 'A', 'F', 'G', 'K', 'M']


def main():


if __name__ == '__main__':
    main()
