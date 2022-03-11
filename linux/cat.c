// ��θ� ���� ������ ���α׷���

// ���μ������� ������ �аų� �� �� Ȥ�� �ٸ� ���μ����� �����͸� �ְ� ���� ��
// ��Ʈ���� ����� �̶� ���� ��ũ���Ͷ�� ���� ���

// ���� ��ũ���� : Ŀ���� ��Ʈ���� �� �� �ο��ϴ� ��ȣ
// 0: STDIN_FILENO, 1: STDOUT_FILENO, 2: STDERR_FILENO

#include <fcntl.h> //open flags(O_RDONLY)
#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <sys/types.h> // ssize_t ���� ��� ����
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
