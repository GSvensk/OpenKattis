#include <stdio.h>
#define _USE_MATH_DEFINES
#include <math.h>
#include <stdlib.h>


int main() {

    double r;
    double area, area_taxi;

    scanf("%lf", &r);
		
    area = pow(r, 2)*M_PI;
    area_taxi = pow(r, 2)*2;
		
    printf("%f\n", area);
    printf("%f\n", area_taxi);
		
    return 0;
}