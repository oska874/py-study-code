#include "p22.h"

float great_circle(float lon1,float lat1,float lon2,float lat2)
{ 
    float radius = 3956.0 ; 
    float pi = 3.14159265;  
    float x = pi/180.0  ;
    float a,b,theta,c  ;
  
    a = (90.0-lat1)*(x)  ;
    b = (90.0-lat2)*(x)  ;
    theta = (lon2-lon1)*(x)  ;
    c = acos((cos(a)*cos(b)) + (sin(a)*sin(b)*cos(theta)));
    return radius * c;
}
 
