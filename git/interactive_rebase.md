# Interactive Rebase
## Outline
두개의 브랜치를 합치는 용도로 쓰이는 `git rebase`에서 `-i`를 추가하여 대화형으로 과거 커밋 히스토리를 수정할 수 있다. 이를 **interactive rebase**라고 한다. 터미널에서 사용하려면 다음과 같이 명령어를 입력하면 된다.

    git rebase -i ${수정할 커밋의 이전 커밋}

위 명령어를 입력하면 텍스트 에디터가 나오면서 과거 커밋들의 히스토리들과 각 커밋을 어떻게 처리할 지에 대한 명령어가 나온다.

이때 주의할 점은 보통 커밋 로그를 보면 밑으로 갈수록 오래된 로그인데 반해 interactive rebase에서 보는 커밋 히스토리는 **위에 있을수록 오래된 로그**이다.


**이미지 수정 필요**

![](2021-11-20-15-17-18.png)

## 명령어
### pick
`pick`은 해당 커밋을 수정하지 않고 그냥 사용하는 명령어이다.

### reword
`reword`은 커밋 메시지를 수정하는 명령어이다.

### edit
`edit`은 해당 커밋은 사용하지만 잠시 멈춰서 작업내용을 수정하거나 추가로 커밋을 넣을 수 있다. edit 123abc이면 123abc 커밋이 된 상태로 가서 멈춘다.