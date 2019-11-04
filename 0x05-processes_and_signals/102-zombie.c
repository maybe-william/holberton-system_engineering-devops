#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * infinite_while - do an infinite while loop
 * Return: 0
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
 * main - the main function
 * Return: 0 or 1 always
 */
int main(void)
{
	int i = 0;
	pid_t f = 0;

	while (i < 5)
	{
		f = fork();
		if (f == 0)
		{
			return (0);
		}
		else
		{
			printf("Zombie process created, PID: %d\n", f);
		}
		i++;
	}
	return (infinite_while());
}
