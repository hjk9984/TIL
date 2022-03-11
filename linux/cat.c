// 모두를 위한 리눅스 프로그래밍

// 프로세스에서 파일을 읽거나 쓸 때 혹은 다른 프로세스와 데이터를 주고 받을 떄
// 스트림을 사용함 이때 파일 디스크립터라는 것을 사용

// 파일 디스크립터 : 커널이 스트림을 열 때 부여하는 번호
// 0: STDIN_FILENO, 1: STDOUT_FILENO, 2: STDERR_FILENO

#include <fcntl.h> //open flags(O_RDONLY)
#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <sys/types.h> // ssize_t 등이 들어 있음
#include <unistd.h>    //system call

static void do_cat(const char *);
static void die(const char *);

int main(int argc, char *argv[])
{
    int i;
    if (argc < 2)
    {
        fprintf(stderr, "%s: file name not given\n", argv[0]);
        exit(1);
    }

    for (i = 1; i < argc; i++)
    {
        do_cat(argv[i]);
    }
    exit(0);
}

static void do_cat(const char *path)
{
    int fd;
    unsigned char buf[1024];
    int n;

    fd = open(path, O_RDONLY); // file descriptor return
    printf("file descriptor : %d\n", fd);
    if (fd < 0)
        die(path);

    while ((n = read(fd, buf, sizeof buf)) > 0)
        if (write(STDOUT_FILENO, buf, n) < 0)
            die(path);

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
