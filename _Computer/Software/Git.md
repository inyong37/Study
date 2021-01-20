# Git | [Homepage](https://git-scm.com/)
Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.

Git is easy to learn and has a tiny footprint with lightning fast performance. It outclasses SCM tools like Subversion, CVS, Perforce, and ClearCase with features like cheap local branching, convenient staging areas, and multiple workflows.[Ref]

### Status

#### Project Status
3 status: Git Directory | Working Directory | Staging Area
- Git Directory: git이 프로젝트의 모든 정보를 저장하는 곳으로, git을 새로 만들거나 clone할 때 git directory가 만들어진다.
- Working Directory: 프로젝트의 특정 버전을 git directory로부터 checkout 상태이다.
- Staging Area: commit할 파일에 대한 정보를 저장한다. 단순한 파일이고 실제로 git directory 내에 존재한다.

Working directory에서 파일을 수정하고, staging area에 파일을 stage해서 commit할 snapshot을 만들고, staging area에 있는 파일들을 commit해서 git directory에 영구적인 snapshot으로 저장한다.

Working Directory | Staging Area | Local Repository | Remote Repository
- git add: working dir -> staging area
- git commit: staging area -> local repo
- git push: local repo -> remote repo
- git fetch: local repo <- remote repo
- git checkout: working dir <- local repo
- git merge: working dir <- local repo

#### File Status
4 status: Untracked | Unmodified | Modified | Staged
- add the file: Untracked -> Staged
- Edit the file: Unmodified -> Modified
- Stage(add) the file: Modified -> Staged
- Remove the file: Untracked <- Unmodified
- Commit: Unmodified <- Staged


### Branch
#### Make branch
- `git branch branch_name`
#### Make and change branch
- `git checkout -b branch_name`
#### Move to branch
- `git checkout branch_name`
#### Delete branch
- `git branch -d branch_name`
#### Delete branch in force
- `git branch -D branch_name`
#### Delete remote branch after deleting local branch
#### Case 1
- `git push origin --delete branch_name`
#### Case 2
- `git branch -d branch_name`
- `git push origin :branch_name`

### Cherry-Pick
다른 브랜치에 있는 commit을 내 브랜치에 적용하는 방법이다.
- conflict가 발생해서 해결하기: conflict를 수정하고 `--continue` 하고 commit message를 수정해서 cherry-pick 마무리한다.
- conflict가 발생해서 취소하기: `--abort`하면 된다.

### Clean

### Clone

#### Clone with HTTPS
- `git clone https://github.com/inyong37/Study.git`

#### Clone with SSH
- `git clone git@github.com:inyong37/Study.git`

#### Clone with GitHub CLI
- `git clone gh repo clone inyong37/Study`

#### Clone single branch
- `git clone -b branch_name --single-branch https://github.com/inyong37/Study.git`

#### Fetch after cloning single branch
- `git remote set-branches --add origin remote_branch_name`
- `git fetch origin remote_branch_name:local_branch_name`

### Error

#### Error: RPC failed
파일의 크기가 클 때 발생할 수 있다. 이때는 buffer의 크기를 크게 해주면 된다.
- `git config --global http.postBuffer`

#### Error: "path_name" already exists in the index
해당 "path_name"이 사용 중인 경우, 예를 들어 안에 다른 folder 또는 file이 있는 경우에 발생한다. 해결책으로는 다른 path를 사용해야한다.
- `git submodule add git@github.com:user_name/submodule_name path_name`

### Hook

### Log
commit log를 볼 수 있다.
- `git log`
- n개의 log만 보기: `git log -n`
  
## Rebase
- commit 2개 합치기: `git rebase -i HEAD~2`
  - `pick` commit# -> `fixup` commit#
- 현재 브랜치의 base를 origin(remote)의 master 브랜치로 업데이트하기: `git rebase origin/master`

### Reflog
project/repository의 git log가 아닌 현재 작업 중인 git log 전체를 볼 수 있다.
- `git reflog`
- 이전 commit HEAD@{1}으로 돌아가기: `git reset --hard HEAD@{1}`

### Remote

#### Show Remote
`git remote`
`git remote -v` with name and url

#### Rename Remote
`git remote rename old_name new_name`

#### Add Remote
`git remote add new_name git@1.1.1.1:user_name/repo_name.git`

#### Remove Remote
`git remote remove delete_name`

### Rename
git으로 버전 관리할 경우, 파일이나 폴더의 이름 변경도 추적할 수 있어야 한다. 특히 리팩토링 때 클래스나 패키지 폴더의 이름 변경은 자주 발생하는 작업이므로 변경 내역을 잘 관리해야 하며 git의 명령어 `git mv`를 사용하면 된다. 바로 stage에 올라간다. unstage로 작업하고 싶다면 `git mv`가 아닌 방식으로 한 뒤 `git add`를 하면 된다. 
- `git mv old_name new_name`

#### Rename: invalid argument
파일이나 폴더 이름의 일부를 대소문자로 변경하는 경우에 발생한다. 이 경우에는 임시 이름으로 한 뒤 변경하는 단계를 거치도록 한다.
- error: `git mv old_name OLD_NAME`
- sol: `git mv old_name temp_name`, `git mv temp_name OLD_NAME`

### Reset
git 명령을 되돌린다.
- `git reset --soft`: commit 명령을 되돌린다. HEAD만 되돌아간다.
- `git reset --mixed`(default): commit, add 명령을 되돌린다. HEAD, index가 되돌아간다.
- `git reset --hard`: commit, add, working dir을 되돌린다. HEAD, index, working dir가 되돌아간다. 이후의 commit history까지 삭제된다.
  - revert의 경우에는 되돌아간다는 commit을 생성한다.

### Restore
git 2.23.0 부터 modified 된 파일을 restore하는 command이다. 이전의 checkout의 기능을 세분화한 것이다.
- `git restore file_name` = `git checkout file_name`

### Submodule
#### Add Submodule: `git submodule add git@github.com:user_name/submodule_name path_name`
#### Delete Submodule
1. `git submodule deinit -f submodule_name`
2-a. UNIX: `rm -rf .git/modules/submodule_name`
2-b. Windows: `rd /s /q .git/modules/submodule_name`
3. `git rm -f path_name/submodule_name`

### Subtree

### Switch
git 2.23.0 부터 branch를 switch하기 위한 command이다. 이전의 checkout의 기능을 세분화한 것이다.
- `git switch branch_name` = `git checkout branch_name`

### Token
- How to setup GitHub token in config file
  - `git config --global github.token`

----------------------------------------------------------------------------------------------------

## Github | [Homepage](https://github.com/)
GitHub is how people build software, it's supporting a community where more than 50 million people learn, share, and work together to build software. First commit was October 2007, headquarters is at San Francisco, and Repositories hosted about 100 million.

## GitLab| [Homepage](https://about.gitlab.com/) | [Source Code](https://github.com/gitlabhq)
GitLab은 Git의 원격 저장소 기능과 이슈 트래커 기능 등을 제공하는 소프트웨어다. 설치형 GitHub라는 컨셉으로 시작된 프로젝트이기 때문에 GitHub와 비슷한 면이 많이 있다. 서비스형 원격저장소를 운영하는 것에 대한 비용이 부담되거나, 소스코드의 보안이 중요한 프로젝트에 적당하다. 설치형 버전관리 시스템으로 자신의 서버에 직접 설치해서 사용할 수 있다. 클라우드 버전 관리 시스템은 gitlab.com을 이용하면 서버 없이도 GitLab의 기능을 이용할 수 있다. 10명 이하의 프로젝트는 무료로 사용할 수 있다. [Ref]

----------------------------------------------------------------------------------------------------

## Git Tutorial Game | [Homepage](https://learngitbranching.js.org/)
- See tutorials command: `levels`
### i. Local
### A. Intro
#### a. level intro1
- resolving deltas
- `git commit`
```
git commit; git commit
```
#### b. level intro2
- `git branch newImage`
- `git checkout newImage; git commit`
```
git branch bugFix; git checkout bugFix
```
#### c. level intro3
- `git merge bugFix`
```
git branch bugFix; git checkout bugFix; git commit; git checkout master; git commit; git merge bugFix
```
#### d. level intro4
- `git rebase master`
```
git branch bugFix; git checkout bugFix; git commit; git checkout master; git commit; git checkout bugFix; git rebase master
```
### B. Ramp Up
#### a. level rampup1
- HEAD: `git checkout C1`
```
git checkout C4
```
#### b. level rampup2
- `fed2da64c0efc5293610bdd892f82a58e8cbc5d8` -> 고유값 `fed2`
- `^`, `~<num>`
- `git checkout master^`
```
git checkout C4; git checkout HEAD^
```
#### c. level rampup3
- `git checkout HEAD~4`
- `git branch -f master HEAD~3`
```
git branch -f master C6; git checkout HEAD^; git branch -f bugFix HEAD~1
```
#### d. level rampup4
- `git reset HEAD~1`: local
- `git revert HEAD`
```
git reset local^; git checkout pushed; git revert pushed
```
#### C. Move
#### a. level move1
- `git cherry-pick C1 C3`
```
git cherry-pick C3 C4 C7
```
#### b. level move2
- `git rebase -i HEAD~4`
- mouse drag & drop, `pick`, and squash
- `undo`, `reset`
```
git rebase -i HEAD~4; # omit C2, change C4 and C5
```
#### D. Mixed
#### a. level mixed1
- `git cherry-pick`
- `git rebase -i`
```
git checkout master; git cherry-pick C4
```
#### b. level mixed2
-  `git rebase -i`, `git commit --amend`, `git rebase -i` 
```
git rebase -i HEAD~2; git commit --amend; git rebase -i HEAD~2; git checkout master; git rebase caption
```
#### c. level mixed3
- `git cherry-pick C2`
```
git checkyout master; git cherry-pick C2; git branch -f master HEAD^; git cherry-pick C2 C3
```
#### d. level mixed4
- `git tag v1 C1`
```
git tag v0 C1; git tag v1 C2; git checkout v1; 
```
#### e. level mixed5
- `git describe <ref>`, `tag`: the nearest (parnet) tag, `numCommits`: distance from tag, `<hash>`: commit hash
```
git describe master; git describe side; git describe bugFix; git commit
```
#### E. Advanced
#### a. level advanced1
- My Solution: `git checkout bugFix; git rebase master; git checkout master; git rebase bugFix; git checkout side; git rebase master side; git checkout master; git rebase side; git checkout another; git rebase master anotherl git checkout master; git rebase another`
- Solution: `git rebase master bugFix; git rebase bugFix side; git rebase side another; git rebase another master`
#### b. level advanced2
- `~`, `^`
- First parent HEAD `git checkout master^`
- Second parent HEAD `git checkout master^2`
- `git checkout HEAD~; git checkout HEAD^2; git checkout HEAD~2` = `git checkout HEAD~^2~2`
- My Solution: `git checkout master~1^2~1; git branch HEAD bugWork; git checkout master`
- Solution: `git branch bugWork master^^2^`
#### c. level advanced3
- `show solution`
- My Solution: `git checkout three; git rebase C2; git checkout one; git cherry-pick C4 C3 C2; git checkout two; git cherry-pick C5 C4 C3 C2`
- Solution: `git checkout one; git cherry-pick C4 C3 C2; git checkout two; git cherry-pick C5 C4 C3 C2; git branch -f three C2`
#### ii. Remote
#### A. Remote
#### a. level remote1
- `git clone`
- Solution: `git clone`
#### b. level remote2
- `<remote name>/<branch name>`
- `o/master` = 브랜치 이름은 `master`, 저장소 이름은 `o` 이다.
- `origin/master` = 브랜치 이름은 `maseter`, 저장소 이름은 `origin` 이다.
- `git checkout o/master; git commit`
- Solution: `git commit; git checkout o/master; git commit`
#### c. level remote3
- `git fetch`: remote repository/storage -> local repository/storage
- Protocol: `http://`, `git://`
- Solution: `git fetch`
#### d. level remote4
- `git pull` = `git fetch` + `git merge`
- `git cherry-pick o/master` = `git rebase o/master` = `git merge o/master`
- Solution: `git pull`
#### e. level remote5
- `git fakeTeamwork foo 3` = 3 commits push to remote
- Solution: `git clone; git fakeTeamwork master 2; git fetch; git commit; git merge`, `git clone; git fakeTeamwork master 2; git commit; git pull;`
#### f. `level remote6`
- `git push`, `push default`
- Solution: `git commit; git commit; git push`
#### g. level remote7
- `git fetch; git rebase o/master; git push`
- + `git fetch; git merge o/master; git push`
- = `git pull --rebase; git push` = `git pull; git push`
- Solution: `git clone; git fakeTeamwork; git commit; git pull --rebase; git push`
#### h. level remote8
- `reset`
- Solution: `git reset o/master; git checkout -b feature C2; git push origin feature`
#### B. Remote Advanced
#### a. level remoteAdvanced1
- My Solution: `git fetch; git checkout side1; git rebase o/master; git checkout side2; git rebase side1; git checkout side3; git rebase side2; git checkout master; git rebase side3; git push`
- Solution: `git fetch; git rebase o/master side1; git rebase side1 side2; git rebase side2 side3; git rebase side3 master; git push`

#### Reference
- Git Log Quit, https://stackoverrun.com/ko/q/2483042, 2020-03-10-Tue.
- Git, https://opentutorials.org/course/785/4933, 2020-07-06-Mon.
- GitLab, https://about.gitlab.com/, 2020-07-06-Mon.
- Remote Branch, https://git-scm.com/book/ko/v2/Git-%EB%B8%8C%EB%9E%9C%EC%B9%98-%EB%A6%AC%EB%AA%A8%ED%8A%B8-%EB%B8%8C%EB%9E%9C%EC%B9%98, 2020-07-06-Mon.
- Submodule, https://git-scm.com/book/ko/v2/Git-%EB%8F%84%EA%B5%AC-%EC%84%9C%EB%B8%8C%EB%AA%A8%EB%93%88, 2020-07-06-Mon.
- rename, https://www.lesstif.com/gitbook/git-git-rename-file-or-folder-54952878.html, 2020-08-24-Mon.
- GitHub about, https://github.com/about, 2020-08-24-Mon.
- rename repo, http://minsone.github.io/git/github-managing-remotes-renaming-a-remote, 2020-08-24-Mon.
- Git, https://git-scm.com/, 2020-08-24-Mon.
- git file status, https://seonkyukim.github.io/git-tutorial/git-status/#, 2020-08-24-Mon.
- git project status, https://ohgyun.com/351, 2020-08-24-Mon.
- git reflog, https://88240.tistory.com/284,2020-08-24-Mon.
- git remote, https://git-scm.com/book/ko/v2/Git%EC%9D%98-%EA%B8%B0%EC%B4%88-%EB%A6%AC%EB%AA%A8%ED%8A%B8-%EC%A0%80%EC%9E%A5%EC%86%8C, 2020-08-24-Mon.
- git submodule deinit blog KR, http://snowdeer.github.io/git/2018/08/01/how-to-remove-git-submodule/, 2020-12-16-Wed.
- error: RPC failed Solution Blog KR, https://gomcine.tistory.com/entry/Git-Push-%EC%8B%9C-%EC%97%90%EB%9F%AC-%ED%95%B4%EA%B2%B0-Failed-with-error-RPC-failed-curl-18-transfer-closed, 2021-01-13-Wed.
- Setup GitHub Token Blog US, https://github.blog/2008-10-11-local-github-config/, 2021-01-13-Wed.
