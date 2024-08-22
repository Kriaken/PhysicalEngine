import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from simulation import *
import random
import numpy as np

p1 = Particle(Vector(500, 500), Vector(0, 0), 1, 10)
p2 = Particle(Vector(400, 500), Vector(10, 0), 1, 10)
#p3 = Particle(Vector(20, 15), Vector(0, 0), 1, 2)

particles = []

for i in range(0):
    particles.append(Particle(Vector(random.randrange(100, 1400), random.randrange(100, 800)), Vector(random.randrange(-50, 50), random.randrange(-10, 10)), 1, 20))

for i in range(20):
    particles.append(Particle(Vector(random.randrange(100, 300), random.randrange(100, 900)), Vector(0, 0), 10, 10))
#
for i in range(5):
    particles.append(Particle(Vector(random.randrange(100, 300), random.randrange(100, 900)), Vector(0, 0), 1, 30))

#particles = [Particle(Vector(2.1, 2.1), Vector(10, 30), 10, 2)]

#walls = [Wall("top", 0, 0), Wall("bottom", 0, 100), Wall("left", 0, 0), Wall("right", 0, 0)]

def acceleration(t):
    return 20*math.cos(t)

t = 0

positions = []

#while t < 1e5:
#    two_particle_simulation.time_step()
#
#    positions_t = []
#    
#    for particle in two_particle_simulation.particles:
#        positions_t.append(particle.getPosition())
#
#    positions.append(positions_t)
#
#    #print(t,"x1", positions[-1][0].X(), "y1", positions[-1][0].Y(), "x2", positions[-1][1].X(), "y2", positions[-1][1].Y())
#
#    t+=two_particle_simulation.dt*1000
#
#
#
#
#
#fig, ax = plt.subplots()
#
#
#ax.set_xlim([-5, two_particle_simulation.width + 5])
#ax.set_ylim([-5, two_particle_simulation.height + 5])
#
#animated_particles = []
#
#animated_p1, = ax.plot([], [], 'o', color='red', markersize=10)
#animated_p2, = ax.plot([], [], 'o', color='red', markersize=10)
#animated_p3, = ax.plot([], [], 'o', color='red', markersize=10)
#animated_p4, = ax.plot([], [], 'o', color='red', markersize=10)
#animated_p5, = ax.plot([], [], 'o', color='red', markersize=10)
#animated_p6, = ax.plot([], [], 'o', color='red', markersize=10)
#animated_p7, = ax.plot([], [], 'o', color='red', markersize=10)
#animated_p8, = ax.plot([], [], 'o', color='red', markersize=10)
#animated_p9, = ax.plot([], [], 'o', color='red', markersize=10)
#animated_p10, = ax.plot([], [], 'o', color='red', markersize=10)
#
#animated_p, = ax.plot([], [], 'o', color='red', markersize=10)
#
#def update_frame(frame):
#    #for j in range(len(particles)):
#    #    animated_pj = animated_p.set_data([positions[frame][j].X()], [positions[frame][j].Y()])
#    #    animated_particles.append(animated_pj)
#
#    animated_p1.set_data([positions[frame][0].X()], [positions[frame][0].Y()])
#    animated_p2.set_data([positions[frame][1].X()], [positions[frame][1].Y()])
#    animated_p3.set_data([positions[frame][2].X()], [positions[frame][2].Y()])
#    animated_p4.set_data([positions[frame][3].X()], [positions[frame][3].Y()])
#    animated_p5.set_data([positions[frame][4].X()], [positions[frame][4].Y()])
#    animated_p6.set_data([positions[frame][5].X()], [positions[frame][5].Y()])
#    animated_p7.set_data([positions[frame][6].X()], [positions[frame][6].Y()])
#    animated_p8.set_data([positions[frame][7].X()], [positions[frame][7].Y()])
#    animated_p9.set_data([positions[frame][8].X()], [positions[frame][8].Y()])
#    animated_p10.set_data([positions[frame][9].X()], [positions[frame][9].Y()])
#
#    return animated_p1, animated_p2, animated_p3, animated_p4, animated_p5, animated_p6, animated_p7, animated_p8, animated_p9, animated_p10
#
#animation = FuncAnimation(fig=fig, frames=int(1e5/(1e3/60)), interval=1000/60, func=update_frame, blit=True,)
#
#animation.save("sim.gif")
#
#plt.plot([positions[-1][0].X()], [positions[-1][0].Y()], markersize=4, color='red')
#plt.show()
#

WIDTH = 400
HEIGHT = 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

walls = [Wall("top", 0, 0), Wall("bottom", acceleration, 0), Wall("left", 0, 0), Wall("right", 0, 0)]

simulation = Simulation(particles, walls, 0.9*WIDTH, 0.9*HEIGHT, Vector(0, 10), 1000/60, 1)

simulating = True

while simulating:

    simulation.time_step()
    simulation.draw(SCREEN)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            simulating = False