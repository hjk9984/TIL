#include <getopt.h>
#include <regex.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static void do_grep(regex_t *pat, FILE *f);

int opt_i = 0;

int main(int argc, char *argv[])
{
    // option parsing
    regex_t pat;
    int opt, i, err;
    while ((opt = getopt(argc, argv, "i")) != -1)
    {
        switch (opt)
        {
        case 'i':
            opt_i = 1;
            break;
        case '?':
            printf("Usage : grep [ option ... ] [ file ... ]\n");
            exit(1);
        }
    }

    // regex pattern lower case
    int re_mode = REG_EXTENDED | REG_NOSUB | REG_NEWLINE;
    if (opt_i)
        re_mode |= REG_ICASE;
    err = regcomp(&pat, argv[optind], re_mode);

    //
    // open stream
    if (argc < 2)
    {
        printf("Usage : grep [ option ... ] [ file ... ]\n");
        exit(1);
    }

    for (i = optind + 1; i < argc; i++)
    {
        FILE *f = fopen(argv[i], "r");
        if (!f)
        {
            perror(argv[i]);
            fclose(f);
        }

        do_grep(&pat, f);

        fclose(f);
    }
    regfree(&pat);
    exit(0);
}

static void do_grep(regex_t *pat, FILE *f)
{
    char buf[4096];
    while (fgets(buf, sizeof buf, f))
    {
        if (regexec(pat, buf, 0, NULL, 0) == 0)
            fputs(buf, stdout);
    }
}
