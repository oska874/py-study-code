import timeit    
  
lon1, lat1, lon2, lat2 = -72.345, 34.323, -61.823, 54.826  
num = 500000  
  
t = timeit.Timer("p2.great_circle(%f,%f,%f,%f)" % (lon1,lat1,lon2,lat2),"import p2")
print "cpython function", t.timeit(num), "sec"  

t = timeit.Timer("p1.great_circle(%f,%f,%f,%f)" % (lon1,lat1,lon2,lat2),"import p1")
print "Pure python function", t.timeit(num), "sec"  

t = timeit.Timer("wrap_p22.great_circle(%f,%f,%f,%f)" % (lon1,lat1,lon2,lat2),"import wrap_p22")
print "pure cython function", t.timeit(num), "sec"  
