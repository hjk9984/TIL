#include <getopt.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define DEFAILT_N_LINES 5

static void do_head(FILE *f, int nlines);

int main(int argc, char *argv[])
{
    int opt, i;
    int n_lines = DEFAILT_N_LINES;

    // option parsing
    while ((opt = getopt(argc, argv, "n:")) != -1) // return -1 when reaching end of options.
    {
        switch (opt)
        {
        case 'n':
            n_lines = atoi(optarg); // optarg is declared in getopt.h
            break;
        case '?':
            fprintf(stdout, "Usage : %s [-n LINES] [FILE ...]\n", argv[0]);
            exit(1);
        }
    }

    for (i = optind; i < argc; i++)
    {
        FILE *f = fopen(argv[i], "r");
        do_head(f, n_lines);
        fclose(f);
    }
    exit(0);
}

static void do_head(FILE *f, int nlines)
{
    int c;

    if (nlines <= 0)
        return;

    while ((c = getc(f)) != EOF)
    {
        if (putchar(c) < 0)
            exit(1);
        if (c == '\n')
        {
            nlines--;
            if (nlines == 0)
                return;
        }
    }
}
