# gitignore 정리
**gitignore 패턴**
> #는 주석을 의미한다.
> 
> /로 시작하면 하위 디렉토리는 무시한다. (not recursivity)
> 
> 디렉터리는 /를 끝에 사용하는 것으로 표현한다.
>
> !로 시작하면 파일은 무시하지 않는다.

**Example**

    # comment of git ignore
    # ignore all .log files
    *.log

    # exclude a.log from *.log
    !a.log

    # ignore the b.py file in current directory except subdir
    /b.py

    # ignore all files in any directory named tmp
    tmp/

    # ignore doc/notes.txt, but not doc/server/arch.txt
    doc/*.txt

    # ignore all .pdf files in the doc/ directory and any of its subdir
    # /** matches 0 or more directories
    doc/**/*.pdf

## **참고**
[www.gitignore.io](www.gitignore.io)을 통해서 간편하게 gitignore 파일을 만들 수 있다.