#include <stdlib.h>
#include <time.h>
#include <sys/time.h>
#include <string.h>
#include <stdio.h>
#include <unistd.h>


int main(void){
	int i = 0;
	while(1){
		printf("%d\n", i);
		printf("%d\n", i);
		printf("%d\n", i);
		printf("\033[3A");
		printf("\033[K");
		i++;
		usleep(1);
	}
	return 0;
}
