# GIT

## 초기 설정

- 최초 한 번만 설정합니다. 

1. 누가 커밋을 남겼는지 확인할 수 있도록 이름과 이메일을 설정합니다.

```bash
$ git config --global user.name 이름
$ git config --global user.email 이메일
```

2. 설정된 내용 확인

```bash
$ git config --global --list
# or
$ git config --global -l
```



### git init

- 현재 작업 중인 directory git으로 관리

##### 주의 사항

- 이미 master로 관리중인 폴더 내에서 **절대 절대 절대 git init 금지**



###  git status

- Working directory와 Staging Area에 있는 파일들의 현재 상태를 확인
- 상태
  1. `untracked` : git이 관리하지 않는 파일
  2. `tracked` : git이 관리하는 파일
     1. `Unmodified` : 최신 상태
     2. `Modified` : 수정되었지만 commit을 남기기 전
     3. `staged` : Staging area에 반영된 상태



## git add

```bash
# 특정 파일
$ git add file_name.txt

# 특정 폴더
$ git add folder/

# 현재 디렉토리에 속한 모든 파일/폴더
$ git add .
```



## git commit

- staging area에 올라온 파일의 변경 사항을 하나의 버전으로 저장하는 명령어
- `커밋 메세지` 는 현재 변경사항을 기록하는 용도로 사용합니다. 

```bash
$ git commit -m "커밋 메세지"
```



## git log

- 커밋의 내역을 조회할 수 있는 명령어

- 옵션
  - `--oneline` : 한 줄로 축약해서 보여줍니다.
  - `--graph` : 브랜치와 머지 내력을 그래프로 보여주는 명령어
  - `--all` : 모든 브랜치의 내역
  - `--reverse` : 커밋 내역의 순서를 반대로 보여주는 명령어

