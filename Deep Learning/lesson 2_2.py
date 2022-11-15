import numpy as np
import matplotlib.pyplot as plt

N = 6
b = 3

x1 = np.array([0.0, 0.2, 0.4, 0.6, 0.8, 1.0]) #np.random.random(N)
#x2 = x1 + [np.random.randint(10)/10 for i in range(N)] + b
x2 = x1 + np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0]) + b
C1 = [x1, x2]

x1 = np.array([0.0, 0.2, 0.4, 0.6, 0.8, 1.0]) #np.random.random(N)
#x2 = x1 - [np.random.randint(10)/10 for i in range(N)] - 0.1 + b
x2 = x1 - np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5])  - 0.1 + b
C2 = [x1, x2]

f = [0 + b, 1 + b]

w2 = 0.5
w3 = -b * w2
w = np.array([-w2, w2, w3])
for i in range(N):
    x1 = np.array([C1[0][i], C1[1][i], 1])
    y1 = np.dot(w, x1)
    plt.text(C1[0][i], C1[1][i],'{:.1f},{:.1f}'.format(C1[0][i], C1[1][i]))

    x2 = np.array([C2[0][i], C2[1][i], 1])
    y2 = np.dot(w, x2)
    plt.text(C2[0][i], C2[1][i],'.{:.1f},{:.1f}'.format(C2[0][i], C2[1][i]))
    
    if y1 >= 0:
        print('Red C1, {:.1f},{:.1f}, y1={}'.format(C1[0][i], C1[1][i], y1))
    else:
        print('Blue C2, {:.1f},{:.1f}, y1={}'.format(C1[0][i], C1[1][i], y1))

    if y2 >= 0:
        print('Red C1, {:.1f},{:.1f}, y2={}'.format(C2[0][i], C2[1][i], y2))
    else:
        print('Blue C2, {:.1f},{:.1f}, y2={}'.format(C2[0][i], C2[1][i], y2))

plt.scatter(C1[0][:], C1[1][:], s=10, c='red')
plt.scatter(C2[0][:], C2[1][:], s=10, c='blue')
plt.plot(f)
plt.grid(True)
plt.show()
