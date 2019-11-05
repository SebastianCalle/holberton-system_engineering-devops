#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - create an infinity loop
 * Return: 0 always
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main -function that creates 5 zombies process
 * Return: 0 always
 */
int main(void)
{
	pid_t zom;
	int i = 0;

	for (i = 0; i < 5; i++)
	{
		zom = fork();
		if (!zom)
			return (0);
		printf("Zombie process created, PID: %d\n", zom);
	}
	infinite_while();
	return (0);
}
