from skyfield.api import load, Topos
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from pytz import timezone

# Load planetary data
planets = load('de421.bsp')  # JPL ephemeris file
earth = planets['earth']

# Define planets
planet_names = ['mercury', 'venus', 'mars', 'jupiter barycenter', 'saturn barycenter', 'uranus barycenter', 'neptune barycenter']
planet_positions = []

# Get current time
ts = load.timescale()
now = datetime.now(timezone('UTC'))
t = ts.utc(now.year, now.month, now.day, now.hour, now.minute, now.second)

# Calculate positions
for planet in planet_names:
    planet_obj = planets[planet]
    astrometric = earth.at(t).observe(planet_obj)
    ra, dec, distance = astrometric.radec()
    planet_positions.append((ra.hours, dec.degrees))

# Plotting
plt.figure(figsize=(8, 8))
for i, (ra, dec) in enumerate(planet_positions):
    plt.scatter(ra, dec, label=planet_names[i].capitalize())

plt.xlabel('Right Ascension (hours)')
plt.ylabel('Declination (degrees)')
plt.title('Real-Time Solar System Positions')
plt.legend()
plt.grid(True)
plt.show()
