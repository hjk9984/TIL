#include <dirent.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

#define INIT_SIZE 1024

struct strBuf
{
    char *buf;
    int len;
};

static void traverse(struct strBuf *);
static void init_str(struct strBuf *);
static void realloc_str(int, struct strBuf *);

int main(int argc, char *argv[])
{
    struct strBuf *strbuf = (struct strBuf *)malloc(sizeof(struct strBuf));
    init_str(strbuf);
    realloc_str(strlen(argv[1]), strbuf);
    strcpy(strbuf->buf, argv[1]);
    traverse(strbuf);
    exit(0);
}

static void traverse(struct strBuf *strbuf)
{

    struct dirent *ent;
    struct stat st;
    DIR *d = opendir(strbuf->buf);
    if (!d)
    {
        perror(strbuf->buf);
        exit(1);
    }

    puts(strbuf->buf);
    while (ent = readdir(d))
    {
        if (strcmp(ent->d_name, ".") == 0)
            continue;
        if (strcmp(ent->d_name, "..") == 0)
            continue;
        realloc_str(strbuf->len + 1 + strlen(ent->d_name) + 1, strbuf);
        if (strcmp(strbuf->buf, "/") != 0)
            strcat(strbuf->buf, "/");
        strcat(strbuf->buf, ent->d_name);
        if (lstat(strbuf->buf, &st) >= 0)
        {
            if (S_ISDIR(st.st_mode)) //) && !S_ISLINK(st.st_mode))
                traverse(strbuf);
            else
                puts(strbuf->buf);
        }
        *strrchr(strbuf->buf, '/') = '\0';
    }
    closedir(d);
}

static void init_str(struct strBuf *strbuf)
{
    strbuf->buf = (char *)malloc(INIT_SIZE);
    if (!strbuf->buf)
        exit(1);
    strbuf->len = INIT_SIZE;
}
static void realloc_str(int len, struct strBuf *strbuf)
{
    if (len < strbuf->len)
        return;

    char *tmp = (char *)realloc(strbuf->buf, len);
    if (!tmp)
        exit(1);
    strbuf->buf = tmp;
    strbuf->len = len;
}
