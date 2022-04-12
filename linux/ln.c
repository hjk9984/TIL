#include <getopt.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int opt_symbolic = 0;

static void do_ln(const char *src, const char *dest);

int main(int argc, char *argv[])
{
    int opt, i;
    while ((opt = getopt(argc, argv, "s")) != -1)
    {
        switch (opt)
        {
        case 's':
            opt_symbolic = 1;
            break;
        case '?':
            fprintf(stderr, "%c : wrong option", optopt);
            exit(1);
        }
    }

    // command check
    printf("%d\n", optind);
    if (argc != optind + 2)
    {
        fprintf(stderr, "%s : wrong arguments\n", argv[0]);
        exit(1);
    }

    // excute ln
    do_ln(argv[1], argv[2]);

    exit(0);
}

static void do_ln(const char *src, const char *dest)
{
    int (*link_func)(const char *, const char *);
    if (opt_symbolic)
        link_func = symlink;
    else
        link_func = link;

    if (link_func(src, dest) < 0)
    {
        perror(src);
        exit(1);
    }
}
