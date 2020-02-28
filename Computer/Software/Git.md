# [Git](https://git-scm.com/)
```
This page is about Git and it's tools.
```
## I. [Github](https://github.com/)

## II. [GitLab](https://about.gitlab.com/)

## III. [Git Tutorial Game](https://learngitbranching.js.org/)
- See tutorials `levels`

### i. Local
### 1-1 `level intro1`
- resolving deltas
- `git commit`
```
git commit; git commit
```

### 1-2 `level intro2`
- `git branch newImage`
- `git checkout newImage; git commit`
```
git branch bugFix; git checkout bugFix
```

### 1-3 `level intro3`
- `git merge bugFix`
```
git branch bugFix; git checkout bugFix; git commit; git checkout master; git commit; git merge bugFix
```

### 1-4 `level intro4`
- `git rebase master`
```
git branch bugFix; git checkout bugFix; git commit; git checkout master; git commit; git checkout bugFix; git rebase master
```

### 2-1 `level rampup1`
- HEAD: `git checkout C1`
```
git checkout C4
```

### 2-2 `level rampup2`
- `fed2da64c0efc5293610bdd892f82a58e8cbc5d8` -> 고유값 `fed2`
- `^`, `~<num>`
- `git checkout master^`
```
git checkout C4; git checkout HEAD^
```

### 2-3 `level rampup3`
- `git checkout HEAD~4`
- `git branch -f master HEAD~3`
```
git branch -f master C6; git checkout HEAD^; git branch -f bugFix HEAD~1
```

### 2-4 `level rampup4`
- `git reset HEAD~1`: local
- `git revert HEAD`
```
git reset local^; git checkout pushed; git revert pushed
```

### 3-1 `level move1`
- `git cherry-pick C1 C3`
```
git cherry-pick C3 C4 C7
```

### 3-2 `level move2`
- `git rebase -i HEAD~4`
- mouse drag & drop, `pick`, and squash
- `undo`, `reset`
```
git rebase -i HEAD~4; # omit C2, change C4 and C5
```

### 4-1 `level mixed1`
- `git cherry-pick`
- `git rebase -i`
```
git checkout master; git cherry-pick C4
```

### 4-2 `level mixed2`
-  `git rebase -i`, `git commit --amend`, `git rebase -i` 
```
git rebase -i HEAD~2; git commit --amend; git rebase -i HEAD~2; git checkout master; git rebase caption
```

### 4-3 `level mixed3`
- `git cherry-pick C2`
```
git checkyout master; git cherry-pick C2; git branch -f master HEAD^; git cherry-pick C2 C3
```

### 4-4 `level mixed4`
- `git tag v1 C1`
```
git tag v0 C1; git tag v1 C2; git checkout v1; 
```

### 4-5 `level mixed5`
- `git describe <ref>`, `tag`: the nearest (parnet) tag, `numCommits`: distance from tag, `<hash>`: commit hash
```
git describe master; git describe side; git describe bugFix; git commit
```

### 5-1 `level advanced1`
#### My Solution
```
git checkout bugFix; git rebase master; git checkout master; git rebase bugFix; git checkout side; git rebase master side; git checkout master; git rebase side; git checkout another; git rebase master anotherl git checkout master; git rebase another
```
#### Solution
```
git rebase master bugFix; git rebase bugFix side; git rebase side another; git rebase another master
```

### 5-2 `level advanced2`
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

### 5-3 `level advanced3`
- `show solution`
#### My Solution
```
git checkout three; git rebase C2; git checkout one; git cherry-pick C4 C3 C2; git checkout two; git cherry-pick C5 C4 C3 C2
```
#### Solution
```
git checkout one; git cherry-pick C4 C3 C2; git checkout two; git cherry-pick C5 C4 C3 C2; git branch -f three C2
```

### ii. Remote
