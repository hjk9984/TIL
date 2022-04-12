#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
    int i;
    if (argc < 2)
    {
        fprintf(stderr, "Usage : mv [ option ... ] file_name1 file_name2\n");
        exit(1);
    }

    // the 'move a file' means that
    // change names of object which is file or dir
    if (rename(argv[1], argv[2]) < 0)
    {
        perror(argv[1]);
        exit(1);
    }
    exit(0);
}
