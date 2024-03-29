import time
import numpy as np
import matplotlib.pyplot as plt

N = 100     # number of elements
Niter = 50  # number of iterations
sigma = 3   # standard deviation
at = 0.5    # value of parameter k
bt = 2      # value of parameter b

aa = 0
bb = 0
lmd1 = 0.000001  # lambda step1
lmd2 = 0.0005    # lambda step2

def E(y, a, b):
    ff = np.array([a * z + b for z in range(N)])
    return np.dot((y-ff).T, (y-ff))

def dEda(y, a, b):
    ff = np.array([a * z + b for z in range(N)])
    return -2*np.dot((y - ff).T, range(N))

def dEdb(y, a, b):
    ff = np.array([a * z + b for z in range(N)])
    return -2*(y - ff).sum()

def an(aa, bb):
  return aa - lmd1 * dEda(y, aa, bb)

def bn(aa, bb):
  return bb - lmd2 * dEdb(y, aa, bb)

f = np.array([at*z+bt for z in range(N)])
y = np.array(f + np.random.normal(0, sigma, N))

a_plt = np.arange(-1, 2, 0.1)
b_plt = np.arange(0, 3, 0.1)
E_plt = np.array([[E(y, a, b) for a in a_plt] for b in b_plt])

plt.ion()   # включение интерактивного режима отображения графиков
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

a, b = np.meshgrid(a_plt, b_plt)
ax.plot_surface(a, b, E_plt, color='y', alpha=0.5)

ax.set_xlabel('a')
ax.set_ylabel('b')
ax.set_zlabel('E')

point = ax.scatter(aa, bb, E(y, aa, bb), c='red')  # отображение точки красным цветом

for n in range(Niter):
    aa = an(aa, bb)
    bb = bn(aa, bb)

    ax.scatter(aa, bb, E(y, aa, bb), c='red')

    # перерисовка графика и задержка на 10 мс
    fig.canvas.draw()
    fig.canvas.flush_events()
    time.sleep(0.01)

    print(aa, bb)

plt.ioff()   # выключение интерактивного режима отображения графиков
plt.show()

# отображение графиков аппроксимации
ff = np.array([aa*z+bb for z in range(N)])

plt.scatter(range(N), y, s=2, c='green')
plt.plot(f)
plt.plot(ff, c='red')
plt.grid(True)
plt.show()


