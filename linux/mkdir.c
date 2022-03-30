#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <sys/types.h>

int main(int argc, char *argv[])
{
    int i;
    // command chaek
    if (argc < 2)
    {
        fprintf(stderr, "%s: no argments\n", argv[0]);
        exit(1);
    }

    // excute mkdir
    for (i = 1; i < argc; i++)
    {
        if (mkdir(argv[i], 0777) < 0) // mode_t >> sys/types
        {
            perror(argv[i]);
            exit(1);
        }
    }

    exit(0);
}
