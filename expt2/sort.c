#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct pair
{
	float x,y;
};

typedef struct pair Pair;

int compare(const void* p,const void* q)
{
	const Pair *a=p,*b=q;
	if(a->x>b->x)
		return 1;
	else
		return -1;
	/*returns >0 if a>b*/
}
int main()
{
	float x2[]={0,11.2,10.14,1.33,1.74,2.27,2.31,2.42,2.54,2.67,2.83,3.03,3.19,3.27,7.63,6.15,5.69,5.42,4.93,4.73,4.57,4.35,4.29,4.19,4.11,4.07,3.86,3.81,3.80,3.68,3.56,3.45,3.94};
	float y2[]={12.06,0.36,0.4,12.07,12.06,11.58,11.4,11.13,10.86,10.48,9.95,9.15,8.5,8.07,0.5,0.64,0.72,0.78,0.96,1.1,1.29,2.16,2.48,3.13,3.63,3.89,5.1,5.37,5.53,6.18,6.86,7.39,4.78};
	int i;
	Pair A[100];
	for(i=0;i<33;i++)
	{
		A[i].x=x2[i];
		A[i].y=y2[i];
	}
	qsort(A,33,sizeof(Pair),compare);
	for(i=0;i<33;i++)
	{
		printf("%f,",A[i].x);
	}
	printf("\n");
	for(i=0;i<33;i++)
	{
		printf("%f,",A[i].y);
	}
}