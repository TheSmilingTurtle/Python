#!/bin/python3

import numpy as np
import tensorflow as tf

import matplotlib.pyplot as plt
import matplotlib.animation as animation

N_BALLS = 2
TIME_STEPS = 5000

y = tf.convert_to_tensor(0.2 + np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1,1)/2, dtype=tf.float32)
X = tf.convert_to_tensor(np.array([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]).T, dtype=tf.float32)

dt = 0.001 #time step
e = 0.3 #coefficient of restitution (kinda)
f = 0.999 #anti-friction

g = 100 #earth gravity almost, maybe, kinda, idk, this is kinda arbitrary actually

p = tf.Variable(tf.random.uniform((X.shape[1] + 1, N_BALLS), minval=-1, maxval=1))

v = tf.Variable(tf.zeros((X.shape[1] + 1, N_BALLS)))

records = [[], [], [], [], [], []]

for _ in range(TIME_STEPS):
    with tf.GradientTape() as tape:
        values = p[:-1]
        tmp = tf.repeat(y, N_BALLS, axis=1) - X @ values
        loss = tf.reduce_mean(tmp * tmp, axis=0)
        grad = -tape.gradient(loss, values)
    
    if not _%100:
        print(f"Completed {_:>5} iterations. Loss: {loss.numpy()}")


    colision = tf.less_equal(p[-1], loss)
    p[-1].assign(tf.where(colision, loss, p[-1]))

    n = tf.pad(grad, tf.constant([[0, 1], [0, 0]]), 'CONSTANT', 1)
    n = tf.linalg.normalize(n, axis=0)[0] #normalize normal vector

    v = tf.where(colision, f * v - e * 2 * tf.repeat(tf.reshape(tf.reduce_sum(v*n, axis=0), (1, -1)), X.shape[1] + 1, axis=0)*n, v) #where a colision happened, reflect velocity along normal, losing some energy in the process r = d - 2*(d*n)n
    v = tf.Variable(v)
    v[-1].assign(v[-1] - g * dt) #accelerate down due to gravity

    p.assign_add(v * dt) # update position

    records[0].append(p[0][0])
    records[1].append(p[1][0])
    records[2].append(p[2][0])
    records[3].append(p[0][1])
    records[4].append(p[1][1])
    records[5].append(p[2][1])

p[-1].assign(loss) #after you are done, project the marbles down onto the loss function, mostly for nicer printing

print()
print(p.numpy())

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

line1 = ax.plot(records[0], records[1], records[2])[0]
line2 = ax.plot(records[3], records[4], records[5])[0]

def update(frame):
    line1.set_xdata(records[0][:frame])
    line1.set_ydata(records[1][:frame])
    line1.set_3d_properties(records[2][:frame])
    line2.set_xdata(records[3][:frame])
    line2.set_ydata(records[4][:frame])
    line2.set_3d_properties(records[5][:frame])
    return (line1, line2)

ani = animation.FuncAnimation(fig=fig, func=update, frames=len(records[0]), interval=1000/len(records[0]), blit=False)
plt.show()