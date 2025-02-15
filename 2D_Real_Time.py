from skyfield.api import load
import matplotlib.pyplot as plt
import time

# Load planetary data
planets = load('de421.bsp')
sun = planets['sun']
ts = load.timescale()

# Define planetary bodies and colors
bodies = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune']
colors = ['gray', 'yellow', 'blue', 'red', 'orange', 'goldenrod', 'lightblue', 'darkblue']

# Set up the figure
plt.ion()  # Enable interactive mode
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')

# Start from current time
t = ts.now()
time_step = 6  # Simulate 6 hours per second for noticeable motion

def plot_solar_system(t):
    ax.clear()  # Clear previous frame
    ax.set_title(f'Solar System (Simulated Time: {t.utc_iso()})')
    ax.set_xlabel('X (AU)')
    ax.set_ylabel('Y (AU)')
    ax.grid(True)  # Enable grid lines

    # Plot each planet
    for body, color in zip(bodies, colors):
        planet = planets[f"{body} barycenter"]
        position = (planet - sun).at(t).position.au
        ax.scatter(position[0], position[1], color=color, label=body.capitalize())

    ax.legend()
    plt.draw()  # Update the figure
    plt.pause(0.1)  # Pause for smooth animation

# Run real-time updating loop
while True:
    plot_solar_system(t)
    t = ts.tt_jd(t.tt + time_step / 24.0)  # Move forward by 'time_step' hours
    time.sleep(1)  # Wait 1 second before next update
