#include <dirent.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

static void do_ls(const char *path);

int main(int argc, char *argv[])
{
    int i;

    // command check
    if (argc < 2)
    {
        fprintf(stderr, "Usage [file...]\n");
        exit(1);
    }

    // excute ls
    for (i = 1; i < argc; i++)
        do_ls(argv[i]);

    exit(0);
}

static void do_ls(const char *path)
{
    // generate DIR stream
    struct dirent *ent;
    DIR *d = opendir(path);
    if (!d)
    {
        perror(path);
        exit(1);
    }

    // read dirent list
    printf("%s file list\n", path);
    while (ent = readdir(d))
        printf("%s\n", ent->d_name);
    printf("\n");

    closedir(d);
}
