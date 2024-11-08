import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

weg_lengte = 120
aantal_autos = 80
max_snelheid = 5
vertraging_kans = 0.3

posities = np.sort(np.random.choice(range(weg_lengte), aantal_autos, replace=False))
snelheden = np.zeros(aantal_autos, dtype=int)

def update_snelheden():
    for i in range(aantal_autos):
        # Versnellen tot max snelheid
        if snelheden[i] < max_snelheid:
            snelheden[i] += 1
            
        # Afremmen als de auto te dichtbij is
        afstand = (posities[(i + 1) % aantal_autos] - posities[i] - 1) % weg_lengte
        if snelheden[i] > afstand:
            snelheden[i] = afstand

        # Willekeurige vertraging
        if np.random.rand() < vertraging_kans:
            snelheden[i] = max(0, snelheden[i] - 1)
def update_posities():
    global posities
    posities = (posities + snelheden) % weg_lengte

fig, ax = plt.subplots()
weg, = ax.plot([], [], 'ro', markersize=8)
ax.set_xlim(0, weg_lengte)
ax.set_ylim(-1, 1)
ax.set_yticks([])

def init():
    weg.set_data([], [])
    return weg,

def animate(frame):
    update_snelheden()
    update_posities()
    weg.set_data(posities, np.zeros(aantal_autos))
    return weg,

ani = animation.FuncAnimation(fig, animate, frames=200, init_func=init, interval=300, blit=True)
plt.show()
