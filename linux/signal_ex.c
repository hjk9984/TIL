// https://www.geeksforgeeks.org/signals-c-language/?ref=lbp

// A signal is a software generated interrupt that is sent to a proc by the os
// There are fix set of signals that can be sent to a process.

#include <signal.h>
#include <stdio.h>
#include <unistd.h>

void handle_sigint(int sig)
{
    printf("Caught signal %d\n", sig);
    printf("if you sent signal again, it will be terminated");
    signal(SIGINT, SIG_DFL); // SIG_IGN is ignore the signal
}

int main()
{
    int i = 15;
    // SIGINT signal's default handler terminates the process
    signal(SIGINT, handle_sigint);
    while (i--)
    {
        printf("hihi\n");
        sleep(1); // unistd.h
    }
    return 0;
}
