# I. [Git](https://git-scm.com/)
```
This page is about Git and it's tools.
```
## i. Commands
### A. Basic
```
git log # show git log
q + 'enter' # exit from git log
```

## ii. Branch
### A. Remote Branch


# II. [Github](https://github.com/)

# III. [GitLab](https://about.gitlab.com/) [Source Code](https://github.com/gitlabhq)

GitLab은 Git의 원격 저장소 기능과 이슈 트래커 기능 등을 제공하는 소프트웨어다. 설치형 GitHub라는 컨셉으로 시작된 프로젝트이기 때문에 GitHub와 비슷한 면이 많이 있다. 서비스형 원격저장소를 운영하는 것에 대한 비용이 부담되거나, 소스코드의 보안이 중요한 프로젝트에 적당하다. 설치형 버전관리 시스템으로 자신의 서버에 직접 설치해서 사용할 수 있다. 클라우드 버전 관리 시스템은 gitlab.com을 이용하면 서버 없이도 GitLab의 기능을 이용할 수 있다. 10명 이하의 프로젝트는 무료로 사용할 수 있다. 

# IV. [Git Tutorial Game](https://learngitbranching.js.org/)

- See tutorials `levels`

## i. Local
### A. Intro
#### a. `level intro1`
- resolving deltas
- `git commit`
```
git commit; git commit
```
#### b. `level intro2`
- `git branch newImage`
- `git checkout newImage; git commit`
```
git branch bugFix; git checkout bugFix
```
#### c. `level intro3`
- `git merge bugFix`
```
git branch bugFix; git checkout bugFix; git commit; git checkout master; git commit; git merge bugFix
```
#### d. `level intro4`
- `git rebase master`
```
git branch bugFix; git checkout bugFix; git commit; git checkout master; git commit; git checkout bugFix; git rebase master
```
### B. Ramp Up
#### a. `level rampup1`
- HEAD: `git checkout C1`
```
git checkout C4
```
#### b. `level rampup2`
- `fed2da64c0efc5293610bdd892f82a58e8cbc5d8` -> 고유값 `fed2`
- `^`, `~<num>`
- `git checkout master^`
```
git checkout C4; git checkout HEAD^
```
#### c. `level rampup3`
- `git checkout HEAD~4`
- `git branch -f master HEAD~3`
```
git branch -f master C6; git checkout HEAD^; git branch -f bugFix HEAD~1
```
#### d. `level rampup4`
- `git reset HEAD~1`: local
- `git revert HEAD`
```
git reset local^; git checkout pushed; git revert pushed
```
### C. Move
#### a. `level move1`
- `git cherry-pick C1 C3`
```
git cherry-pick C3 C4 C7
```
#### b. `level move2`
- `git rebase -i HEAD~4`
- mouse drag & drop, `pick`, and squash
- `undo`, `reset`
```
git rebase -i HEAD~4; # omit C2, change C4 and C5
```
### D. Mixed
#### a. `level mixed1`
- `git cherry-pick`
- `git rebase -i`
```
git checkout master; git cherry-pick C4
```
#### b. `level mixed2`
-  `git rebase -i`, `git commit --amend`, `git rebase -i` 
```
git rebase -i HEAD~2; git commit --amend; git rebase -i HEAD~2; git checkout master; git rebase caption
```
#### c. `level mixed3`
- `git cherry-pick C2`
```
git checkyout master; git cherry-pick C2; git branch -f master HEAD^; git cherry-pick C2 C3
```
#### d. `level mixed4`
- `git tag v1 C1`
```
git tag v0 C1; git tag v1 C2; git checkout v1; 
```
#### e. `level mixed5`
- `git describe <ref>`, `tag`: the nearest (parnet) tag, `numCommits`: distance from tag, `<hash>`: commit hash
```
git describe master; git describe side; git describe bugFix; git commit
```
### E. Advanced
#### a. `level advanced1`
#### My Solution
```
git checkout bugFix; git rebase master; git checkout master; git rebase bugFix; git checkout side; git rebase master side; git checkout master; git rebase side; git checkout another; git rebase master anotherl git checkout master; git rebase another
```
#### Solution
```
git rebase master bugFix; git rebase bugFix side; git rebase side another; git rebase another master
```
#### b. `level advanced2`
- `~`, `^`
- First parent HEAD `git checkout master^`
- Second parent HEAD `git checkout master^2`
- `git checkout HEAD~; git checkout HEAD^2; git checkout HEAD~2` = `git checkout HEAD~^2~2`
#### My Solution
```
git checkout master~1^2~1; git branch HEAD bugWork; git checkout master
```
#### Solution
```
git branch bugWork master^^2^
```
#### c. `level advanced3`
- `show solution`
#### My Solution
```
git checkout three; git rebase C2; git checkout one; git cherry-pick C4 C3 C2; git checkout two; git cherry-pick C5 C4 C3 C2
```
#### Solution
```
git checkout one; git cherry-pick C4 C3 C2; git checkout two; git cherry-pick C5 C4 C3 C2; git branch -f three C2
```
## ii. Remote
### A. Remote
#### a. `level remote1`
- `git clone`
```
git clone
```
#### b. `level remote2`
- `<remote name>/<branch name>`
- `o/master` = 브랜치 이름은 `master`, 저장소 이름은 `o` 이다.
- `origin/master` = 브랜치 이름은 `maseter`, 저장소 이름은 `origin` 이다.
- `git checkout o/master; git commit`
```
git commit; git checkout o/master; git commit
```
#### c. `level remote3`
- `git fetch`: remote repository/storage -> local repository/storage
- Protocol: `http://`, `git://`
```
git fetch
```
#### d. `level remote4`
- `git pull` = `git fetch` + `git merge`
- `git cherry-pick o/master` = `git rebase o/master` = `git merge o/master`
```
git pull
```
#### e. `level remote5`
- `git fakeTeamwork foo 3` = 3 commits push to remote
```
git clone; git fakeTeamwork master 2; git fetch; git commit; git merge
git clone; git fakeTeamwork master 2; git commit; git pull;
```
#### f. `level remote6`
- `git push`, `push default`
```
git commit; git commit; git push
```
#### g. `level remote7`
- `git fetch; git rebase o/master; git push`
- + `git fetch; git merge o/master; git push`
- = `git pull --rebase; git push` = `git pull; git push`
```
git clone; git fakeTeamwork; git commit; git pull --rebase; git push
```
#### h. `level remote8`
- `reset`
```
git reset o/master; git checkout -b feature C2; git push origin feature
```
### B. Remote Advanced
#### a. `level remoteAdvanced1`
#### My Solution
```
git fetch; git checkout side1; git rebase o/master; git checkout side2; git rebase side1; git checkout side3; git rebase side2; git checkout master; git rebase side3; git push
```
#### Solution
```
git fetch; git rebase o/master side1; git rebase side1 side2; git rebase side2 side3; git rebase side3 master; git push
```
#### Reference
- Git Log Quit, https://stackoverrun.com/ko/q/2483042, 2020-03-10-Tue.
- Git, https://opentutorials.org/course/785/4933, 2020-07-06-Mon.
- GitLab, https://about.gitlab.com/, 2020-07-06-Mon.
- Remote Branch, https://git-scm.com/book/ko/v2/Git-%EB%B8%8C%EB%9E%9C%EC%B9%98-%EB%A6%AC%EB%AA%A8%ED%8A%B8-%EB%B8%8C%EB%9E%9C%EC%B9%98, 2020-07-06-Mon.
- Sub Module, https://git-scm.com/book/ko/v2/Git-%EB%8F%84%EA%B5%AC-%EC%84%9C%EB%B8%8C%EB%AA%A8%EB%93%88, 2020-07-06-Mon.
