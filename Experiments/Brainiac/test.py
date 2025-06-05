import numpy as np

from rich.progress import track

X = np.array([[0,1,0,1], 
              [1,0,0,1]])
y = np.array([[0,1,1,0]])

k = 10
epochs = 100
reflection_time = 50
thinking_time = 10

alpha = 0.2
epsilon = alpha
p = 0.2

N = 20

s = np.zeros((thinking_time, y.shape[1]))

for i in track(range(N)):
    A = np.random.normal(size=(X.shape[0]+k+y.shape[0]+1, X.shape[0]+k+y.shape[0]+1))
    A = (A+A.T)/2
    tmp = np.abs(np.diag(A)[:,None])@np.diag(A)[None,:]
    A /= np.sqrt(np.abs(tmp))*np.sign(tmp)

    z = None
    c = None


    for _ in range(epochs):
        z = np.block([[X],
                    [np.ones((1,X.shape[1]))],
                    [np.random.normal(size=(k,X.shape[1]))],
                    [y]])

        B = np.zeros_like(A)
        mask = np.logical_and(np.random.rand(*A.shape)<p, np.eye(A.shape[0]))
        B[mask] = A[mask]

        c = B@z

        # c[:X.shape[0]+1] = z[:X.shape[0]+1]
        # c[-y.shape[0]:] = z[-y.shape[0]:]

        A += alpha*((c[:, None] + c[None, :])/(np.abs(c[:, None] - c[None, :]) + epsilon)).sum(axis=2)
        tmp = np.abs(np.diag(A)[:,None])@np.diag(A)[None,:]
        A /= np.sqrt(np.abs(tmp))*np.sign(tmp)


        for __ in range(reflection_time):
            # c[:X.shape[0]+1] = z[:X.shape[0]+1]
            # c[-y.shape[0]:] = z[-y.shape[0]:]
            c = B@c

            A += alpha*((c[:, None] + c[None, :])/(np.abs(c[:, None] - c[None, :]) + epsilon)).sum(axis=2)
            tmp = np.abs(np.diag(A)[:,None])@np.diag(A)[None,:]
            A /= np.sqrt(np.abs(tmp))*np.sign(tmp)

    z = np.block([[X],
                [np.ones((1,X.shape[1]))],
                [np.random.normal(size=(k,X.shape[1]))],
                [y]])
    
    for i in range(thinking_time):
        z = A@z
        out = z[-y.shape[0]:].flatten()
        s[i][(out-out.min())/(out-out.min()).max()>0.5] += 1
    

print(s/N)
