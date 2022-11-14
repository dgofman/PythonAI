import numpy as np

def format(x, base=0.05):
    return round(base * round(x / base), 2)

def act(x):
    return 0 if x < 0.5 else 1

def go(house, rock, attr):
    x = np.array([house, rock, attr])
    w1 = [0.3, 0.3, 0] #  (house=.3, rock=.3, attr=0) = -1
    w2 = [0.4, -0.5, 1] # (house=.4, rock=-.5, attr=1) = 1
    w3 = [-1, 1] #-1 = No, 1 = YES

    #weight1 = [w1, w2] # np.array([w1, w2])  # 2-D NumPy Arrays 
    #sum_hidden = np.dot(weight1, x) #https://sparkbyexamples.com/numpy/numpy-dot-function/
    sum_hidden = [format(w1[0]*x[0] + w1[1]*x[1] + w1[2]*x[2]), format(w2[0]*x[0] + w2[1]*x[1] + w2[2]*x[2])]
     
    print('First hidden nodes: '+str(sum_hidden))

    out_hidden = np.array([act(x) for x in sum_hidden])
    print('Second hidden nodes: '+str(out_hidden))

    #weight2 = np.array(w3)  # 1-D NumPy Arrays 
    #sum_end = np.dot(weight2, out_hidden)
    sum_end = w3[0]*out_hidden[0] + w3[1]*out_hidden[1]
    y = act(sum_end)
    print('Output nodes: '+str(y))

    return y

def predict(house, rock, attr):
    res = go(house, rock, attr)
    if res == 1:
        print('Yes')
    else:
        print('No')

predict(1, 1, 0)
predict(1, 0, 1)
predict(0, 0, 1)


