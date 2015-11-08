#include <math.h>  
#include <stdio.h>  
#include <unistd.h>
#include <sys/time.h>

#define NUM 500000  
  
float great_circle(float lon1, float lat1, float lon2, float lat2)
{  
    float radius = 3956.0;  
    float pi = 3.14159265;  
    float x = pi/180.0;  
    float a,b,theta,c;  
  
    a = (90.0-lat1)*(x);  
    b = (90.0-lat2)*(x);  
    theta = (lon2-lon1)*(x);  
    c = acos((cos(a)*cos(b)) + (sin(a)*sin(b)*cos(theta)));  
    return radius*c;  
}  
  
int main() 
{  
    int i;  
    float x;  
    struct timeval times,timee;
    gettimeofday(&times,NULL);
    for (i=0; i <= NUM; i++)  
        x = great_circle(-72.345, 34.323, -61.823, 54.826);  
    gettimeofday(&timee,NULL);
    printf("time %f (us)\n",((float)((timee.tv_sec-times.tv_sec)*1000000+timee.tv_usec-times.tv_usec))/1000000);
    return 0;
}  
