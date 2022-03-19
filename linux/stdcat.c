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
    FILE *fp;
    int c;

    // if ((fd = open(path, O_RDONLY)) < 0)

    if (!(fp = fopen(path, "r"))) // if failed, fopen return NULL
        die(path);

    // fgetc(fp);    read 1byte and return the byte read. if failed, return EOF;
    // getc(fp);     getc is macro of fgetc
    // fputc(int c, fp);    if failed, return EOF;

    while ((c = fgetc(fp)) != EOF) // EOF == -1
    {
        // lseek(fd, -5, SEEK_CUR);
        if (fputc(c, stdout) < 0)
            exit(1);
    }

    // if (close(fd) < 0)
    if (fclose(fp) < 0)
        die(path);
}

static void die(const char *s)
{
    perror(s);
    exit(1);
}
