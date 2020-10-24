import numpy as np
import matplotlib.pyplot as plt

N = 60
Y = np.zeros((N,N))

X = np.zeros((N,N),dtype=int)
R = np.random.normal(0,.3,(N,N))
mu = [.2,1.]

for i in range(N):
    for j in range(N):
        if np.sqrt((i-N/2)**2+(j-N/2)**2)<10:
            Y[i,j] = 1+R[i,j]
        else:
            Y[i,j] = .2+R[i,j]

        X[i,j] = np.random.choice([0,1])


Y = np.clip(Y, 0, 1, out=Y)
print(Y)
print(X)
def p_x_given_neighbour(i,j,x):
    p = 1
    beta = 2

    for i_, j_ in [(i + 1, j + 1), (i - 1, j + 1), (i - 1, j - 1), (i + 1, j - 1)]:
        if 0<=i_< N and 0<=j_<N:
            p *= np.exp(-beta*(x-X[i_,j_])**2)
    return p


def p_x(i,j,x):
    s = .3
    return np.exp(-(Y[i,j]-mu[x])**2/s**2)

plt.title("Pixel Values")

plt.imshow(Y)
plt.show()

plt.title("Labels at initialization")

plt.imshow(X)
plt.show()
for k in range(100):
    for i in range(N):
        for j in range(N):
            px = np.array([0.,0.])
            for x in range(0,2):
                px[x] = p_x_given_neighbour(i,j,x)*p_x(i,j,x)


            x_ = np.random.choice([0,1], 1, p=px/np.sum(px))[0]
            X[i,j] = x_

    print(X)
    plt.title("Labels after iteration " + str(k+1))
    plt.imshow(X)
    plt.show()