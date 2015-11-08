cdef extern from "p22.h":
    float _great_circle "great_circle"(float lon1,float lat1,float lon2,float lat2)
def great_circle(lon1,lat1,lon2,lat2):
    ''' Returns the nth Fibonacci number.'''
    return _great_circle(lon1,lat1,lon2,lat2)
