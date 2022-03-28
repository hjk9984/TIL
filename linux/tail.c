#include <getopt.h>
#include <stdio.h>
#include <stdlib.h>

#define DEFAULT_NLINES 5

static void do_tail(FILE *f);

int main(int argc, char *argv[])
{
    int i;

    // check input
    if (argc < 2)
    {
        fprintf(stderr, "Usage: %s < infile\n", argv[0]);
        exit(1);
    }

    // for loop for files
    for (i = 1; i < argc; i++)
    {
        FILE *f = fopen(argv[i], "r");
        if (!f)
            exit(1);

        do_tail(f);
    }
    exit(0);
}

static void do_tail(FILE *f)
{
    int c, nlines = DEFAULT_NLINES;

    // put stream position eof
    if (fseek(f, -1, SEEK_END) < 0)
        exit(1);

    // check new line char
    while (nlines > 0)
    {
        if (fgetc(f) == '\n')
            nlines--;

        if (fseek(f, -2, SEEK_CUR) != 0)
            break;
    }

    // write chars up to EoF
    fseek(f, 2, SEEK_CUR);
    while ((c = fgetc(f)) > 0)
        if (fputc(c, stdout) < 0)
            exit(1);

    if (fclose(f) < 0)
        exit(1);
}
