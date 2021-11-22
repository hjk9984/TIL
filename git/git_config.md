# Git configuration

## Outline
`git config`를 통해 설정 내용을 확인하고 변경할 수 있다. 이때 사용되는 설정 파일은 3가지나 된다.

* `/etc/gitconfig`은 시스템의 모든 사용자와 모든 저장소에 적용되는 설정으로 `git config --system`으로 사용된다.
* `~/.gitconfig`는 사용자에게 적용되는 설정, `git config --global`로 사용된다.
* `.git/config`는 프로젝트(폴더)별로 초기화되어 있는 git 파일로 `--local`로 사용할 수 있다.

위 설정 파일들의 우선순위는 **system < global < local**으로 로컬이 가장 우선시 된다.

## 설정 확인
`git config --list` 명령을 실행하면 설정한 모든 것을 보여주며 `--global`처럼 설정파일을 지정해주면 해당 설정파일에서의 설정한 것만 보여준다.

이때 global과 local이 같은 설정을 가지면 중복되어서 나타날 수 있다.

## 편집기 사용
`git config --global core.editor "code --wait"`를 통해 vscode를 사용하여 설정파일을 수정할 수 있다.


### Reference
https://git-scm.com/book/ko/v2/%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0-Git-%EC%B5%9C%EC%B4%88-%EC%84%A4%EC%A0%95