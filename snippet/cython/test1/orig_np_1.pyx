import numpy as np

cimport numpy as np

def julia(float z0a,float z0b,int scale,float s):
    cdef int N
    N=int(s*scale)
    cdef np.ndarray[np.int_t,ndim=2] p=np.zeros([N,N],dtype=np.int)
    cdef complex z0=complex(z0a,z0b)
    cdef int a,b,color
    cdef complex z
    for a in range(N):
        for b in range(N):
            z=complex((a-0.5*N)/scale,(b-0.5*N)/scale)
            color=0
            for i in range(200):
                if z.real*z.real+z.imag*z.imag>4:
                    color=i
                    break
                else:
                    z=z*z+z0
            p[a,b]=color
    return p
