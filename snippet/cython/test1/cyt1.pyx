import numpy as np

def P0julia(z0a,z0b,scale,s):

    N=int(s*scale)

    p=np.zeros([N,N],dtype=np.int)

    z0=complex(z0a,z0b)

    for a in range(N):

        for b in range(N):

            z=complex((a-0.5*N)/scale,(b-0.5*N)/scale)

            color=0

            for i in range(200):

                if abs(z)>4:

                    color=i

                    break

                else:

                    z=z*z+z0

            p[a,b]=color

    return p
