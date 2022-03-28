#include <stdio.h>

int main()
{
    char buf[1024];

    FILE *f = fopen("test.txt", "r");

    int c = fgetc(f); // returns the read char. if end of file is reached, return EOF(-1)
    fputc(c, stdout);
    fputc('\n', stdout);

    fgets(buf, 1024, f);        // read size - 1 characters or until new line char or EOF. return char array or NULL
    int k = fputs(buf, stdout); // copies char array up to NULL char(\0) to stream.
    // printf("%s\n", buf[k]);
    //  printf("%d\n", k);

    // c = getchar(); // read a char from the stdin stream.
    // putchar(c);

    // scanf("%s", str)
    //  scanf fucntion doesn't limit the maximum size of input char array.
    //  It may causes overflow.

    //
    int sz = fread(buf, 1, 100, f);
    if (sz != 100)
    {
        perror("Reading error : ");
        // exit(2);
    }
    fwrite(buf, 1, sz, stdout);

    //
    //
    if (ferror(f)) // If a error indicator is indicated, return error indicator of the stream, otherwise return 0.
    {
        perror("error is raised\n"); // interprets the errno and outputs the err msg to stdout.
        if (feof(f))
            printf("EOF\n");
        fclose(f);
    }

    fclose(f);
    // close the file corresponding to the stream.
    // At this time, the contents of the butter that have not yet been written to the file
    // are written to the file.
}
