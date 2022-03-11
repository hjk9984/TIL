#include <stdio.h>

// 커멘드 라인에서 실행 파일 뒤에 오는 것을 "실행인자"라고 한다.
// argv는 이차원 배열로 생각할 수 있으며 argv[0]은 ./실행파일이름이다.

int main(int argc, char *argv[])
{
    int i;

    printf("argc = %d\n", argc);
    for (i = 0; i < argc; i++)
    {
        printf("argc[%d]=%s\n", i, argv[i]);
    }
    return 0;
}
