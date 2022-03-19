#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

static void do_cat(const char *path);
static void die(const char *s);

int main(int argc, char *argv[])
{
    int i;
    if (argc < 2)
    {
        unsigned char buf[2048];
        int n = read(STDIN_FILENO, buf, sizeof buf);
        write(STDOUT_FILENO, buf, n);
        // fprintf(stderr, "%s: file name not given\n", argv[0]);
        // exit(1);
    }

    for (i = 1; i < argc; i++)
    {
        do_cat(argv[i]);
    }
}

static void do_cat(const char *path)
{
    int fd;
    char buf[2024];
    int n;

    if ((fd = open(path, O_RDONLY)) < 0)
        die(path);

    while ((n = read(fd, buf, 30)) > 0)
    {
        // lseek(fd, -5, SEEK_CUR);
        write(STDOUT_FILENO, buf, n);
    }

    if (n < 0)
        die(path);
    if (close(fd) < 0)
        die(path);
}

static void die(const char *s)
{
    perror(s);
    exit(1);
}
