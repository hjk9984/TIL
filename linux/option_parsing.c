#include <getopt.h>
#include <stdio.h>

int opt_all = 0;

static struct option longopts[] = {
    {"lines", required_argument, NULL, 'n'},
    {"all", no_argument, &opt_all, 1}, // if this option is used, opt_all will be assigned 1.
    {"help", no_argument, NULL, 'h'},
    {0, 0, 0, 0}
    // last entry must consist of zeros
};

int main(int argc, char *argv[])
{
    int opt;
#if 0

    // there are some global variable related to getopt func.
    while ((opt = getopt(argc, argv, "af:")) != -1) // the order of option doesn't matter
    {
        printf("optopt : %c\n", optopt); // current option char
        printf("optarg : %s\n", optarg); // current option argument
        printf("optind : %d\n", optind);
        switch (opt)
        {
        case 'a':
            break;
        case 'f':
            break;
        case '?': // wrong option
            break;
        }
    }
#endif

    // if getting long option, we need to use getopt_long()
    while ((opt = getopt_long(argc, argv, "n:ah", longopts, NULL)) != -1)
    {
        printf("optopt : %c\n", optopt); // current option char
        printf("optarg : %s\n", optarg); // current option argument
        printf("optind : %d\n", optind);
        switch (opt)
        {
        case 'n':
            printf("n\n");
            break;
        // case 'a':
        //     printf("a\n");
        //     break;
        case 'h':
            printf("h\n");
            break;
        case '?': // wrong option
            break;
        }
    }
}
