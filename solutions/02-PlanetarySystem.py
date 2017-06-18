#!/usr/bin/env python
# -*- coding: utf8 -*-

from __future__ import division

# Own modules
from Star import Star
from Planet import Planet

class PlanetarySystem():
    """
    Class to create objects related with a planetary system
    author: S. Sousa and D. Andreasen
    """
    def __init__(self, star, planet_list):
        self.planets_list = planet_list
        self.star = star

    def __str__(self):
        strout = ""
        for myPlanet in self.planets_list:
            strout += str(myPlanet)
        return strout

    def get_planets_with_life(self):
        ''' Get a list with the planets with life in the system'''
        planet_life_list = []
        for planet in self.planets_list:
            if planet.life:
                planet_life_list.append(planet)
        return planet_life_list

    def get_total_mass_planets(self):
        ''' Sum the masses of the planets in the system'''
        total_mass = 0
        for planet in self.planets_list:
             total_mass+=planet.p_mass
        return total_mass


def main():
    # Create a star named the Sun
    Sun = Star(1.0, 1.0)
    print Sun

    # Data for some 'random' planets from
    # http://hyperphysics.phy-astr.gsu.edu/hbase/solar/soldata2.html
    # http://www.windows2universe.org/our_solar_system/planets_table.html

    # Some totally random names, radii, masses, etc.
    names = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn',
            'Uranus', 'Neptune']
    p_radii = [0.382, 0.949, 1, 0.532, 11.19, 9.44, 4.007, 3.883]
    p_masses = [0.055, 0.815, 1, 0.107, 317.8, 95., 15., 17.]
    eccentricities = [0.206, 0.007, 0.0167, 0.093, 0.048, 0.06, 0.05, 0.05,
            0.01, 0.25]
    periods = [87.969, 224.70, 365.256, 686.98, 4332.71, 10759.5, 30685.0,
            60190.0]
    distances = [0.387, 0.723, 1, 1.524, 5.203, 9.54, 19.18, 30.06]

    # However, intelligent life is not found on any of the planets yet.
    lifes = [False, False, True, False, False, False, False, False]

    # TODO : Instead of making a list, create a dictionary, where the key is
    # the name of the planet...
    myPlanets = []
    for radius, mass, eccentrisity, period, distance, life, name in \
    zip(p_radii, p_masses, eccentricities, periods, distances, lifes, names):
        myPlanets.append(Planet(radius, mass, eccentrisity, period, distance, life))

    my_planetary_system = PlanetarySystem(Star,myPlanets)
    print my_planetary_system

    print "--------------------------------"
    print "-Showing the planets with life:-"
    print "--------------------------------"
    planets_with_life = my_planetary_system.get_planets_with_life()
    for planet in planets_with_life:
        print planet
    print "--------------------------------"
    print "-Total mass of the planets:    -"
    print "--------------------------------"
    print "Total mass: ", my_planetary_system.get_total_mass_planets()


if __name__ == '__main__':
    main()
