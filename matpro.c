#include<stdio.h>
#include<stdlib.h>
#include<sys/time.h>

double get_time(){

	struct timeval tv;
	gettimeofday(&tv,NULL);
	return tv.tv_sec+tv.tv_usec*1e-6;
}

int main(int argc,char **argv){

	if(argc!=2){
		printf("usage:%s N\n",argv[0]);
		return -1;
	}


	int i,j,k;
	int n=atoi(argv[1]);

	double **A=(double**)malloc(n*sizeof(double*));
	double **B=(double**)malloc(n*sizeof(double*));
	double **C=(double**)malloc(n*sizeof(double*));

	for(i=0;i<n;i++){
		A[i]=(double*)malloc(n*sizeof(double));
		B[i]=(double*)malloc(n*sizeof(double));
		C[i]=(double*)malloc(n*sizeof(double));
		for(j=0;j<n;j++){
			A[i][j]=i*n+j;
			B[i][j]=j*n+i;
			C[i][j]=0.0;
		}
	}

	double begin=get_time();

	for(i=0;i<n;i++){
		for(j=0;j<n;j++){
			for(k=0;k<n;k++){
				C[i][j]+=A[i][k]*B[k][j];
			}
		}
	}

	double end=get_time();
	printf("time: %.6lf sec\n", end - begin);

	// double sum=0;
	// for(i=0;i<n;i++){
	// 	for(j=0;j<n;j++){
	// 		sum+=C[i][j];
	// 		printf("C[%d][%d]=%lf\n",i,j,C[i][j]);
	// 	}
	// }

	//printf("sum:%.61f\n",sum);

	free(A);
	free(B);
	free(C);

	return 0;

}