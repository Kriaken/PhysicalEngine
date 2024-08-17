import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from simulation import *

p1 = Particle(Vector(5, 15), Vector(5, 0), 1, 2)
p2 = Particle(Vector(7, 15), Vector(5, 0), 1, 2)
p3 = Particle(Vector(20, 15), Vector(0, 0), 1, 2)

walls = [Wall("top", 0, 0), Wall("bottom", 0, 0), Wall("left", 0, 0), Wall("right", 0, 0)]

two_particle_simulation = Simulation([p1, p2, p3], walls, 100, 100, Vector(0, 0), 1000/60, 1)

t = 0

positions = []

while t < 1e4:
    two_particle_simulation.time_step()

    p1_v = Vector(p1.getPosition().X(), p1.getPosition().Y())
    p2_v = Vector(p2.getPosition().X(), p2.getPosition().Y())
    p3_v = Vector(p3.getPosition().X(), p3.getPosition().Y())

    positions.append([p1_v, p2_v, p3_v])

    #print(t,"x1", positions[-1][0].X(), "y1", positions[-1][0].Y(), "x2", positions[-1][1].X(), "y2", positions[-1][1].Y())

    t+=two_particle_simulation.dt*1000





fig, ax = plt.subplots()


ax.set_xlim([-5, 120])
ax.set_ylim([10, 20])

animated_p1, = ax.plot([], [], 'o', color='red', markersize=10)
animated_p2, = ax.plot([], [], 'o', color='blue', markersize=10)
animated_p3, = ax.plot([], [], 'o', color='blue', markersize=10)

def update_frame(frame):
    animated_p1.set_data([positions[frame][0].X()], [positions[frame][0].Y()])
    animated_p2.set_data([positions[frame][1].X()], [positions[frame][1].Y()])
    animated_p3.set_data([positions[frame][2].X()], [positions[frame][2].Y()])

    return animated_p1, animated_p2, animated_p3 

animation = FuncAnimation(fig=fig, frames=int(1e4/(1e3/60)), interval=1000/60, func=update_frame, blit=True,)

animation.save("sim.gif")

plt.plot([positions[-1][0].X()], [positions[-1][0].Y()], markersize=4, color='red')
plt.show()
