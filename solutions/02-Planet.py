#!/usr/bin/env python
# -*- coding: utf8 -*-

from __future__ import division


class Planet():
    """
    Class to create objects related planets
    author: D. Andreasen
    """
    grav = 6.67384e-11  # Gravitational constant
    au = 149597871  # average distance to the Sun from Earth

    def __init__(self, p_radius, p_mass, ecc, Period, dist, life=False):
        # Assign the parameters for a planet here to the self-object
        self.p_radius = p_radius
        self.p_mass = p_mass
        self.ecc = ecc
        self.Period = Period
        self.dist = dist
        self.life = life

    def get_surface_gravity(self):
        return self.grav * self.p_mass / self.p_radius ** 2

    def __str__(self):
        # This will happen if we print a planet
        string = ''
        string += 'Mass is\t\t\t %.2f\n' % self.p_mass
        string += 'Radius is\t\t %.2f\n' % self.p_radius
        string += 'Surface gravity is\t %s\n' % self.get_surface_gravity()
        if self.life:
            string += '\nLife is found on this planet!!!\n\n'
        else:
            string += '\nNo life detected on this planet...\n\n'

        return string

    @staticmethod
    def planet_types():
        return ['Rocky', 'Water world', 'Puffy', 'Gas giant', 'Unknown']


def main():

    # Make a random planet with life
    planet1 = Planet(5, 10, 0.1, 2.4, 0.02, True)
    print planet1


if __name__ == '__main__':
    main()
