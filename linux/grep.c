#include <regex.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>

static void do_grep(regex_t *pat, FILE *f);

int main(int argc, char *argv[])
{
    regex_t pat;
    int err;
    int i;

    if (argc < 2)
    {
        fputs("no pattern\n", stderr);
        exit(1);
    }

    // convert from char array to regex_t
    // regcomp use memory independently, so use regfree to free it.
    // REG_ICASE >> ignores whether a char is upper or lower case.
    err = regcomp(&pat, argv[1], REG_EXTENDED | REG_NOSUB | REG_NEWLINE);

    if (err != 0)
    {
        char buf[1024];
        // err is error code
        regerror(err, &pat, buf, sizeof buf);
        puts(buf);
        exit(1);
    }

    if (argc == 2)
        do_grep(&pat, stdin);
    else
    {
        int i;
        for (i = 2; i < argc; i++)
        {
            FILE *f;
            f = fopen(argv[i], "r");
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
    regfree(&pat);
    exit(0);
}

static void do_grep(regex_t *pat, FILE *src)
{
    char buf[4096];
    while (fgets(buf, sizeof buf, src))
    {
        if (regexec(pat, buf, 0, NULL, 0) == 0) // return 0 if they match, otherwise an error code.
        {
            fputs(buf, stdout);
        }
    }
}
