# Git
```
This page is about Git and it's tools.
```
## Github

## GitLab

## [Git Tutorial Game](https://learngitbranching.js.org/)

### 1-1
### 1-2
### 1-3
### 1-4
### 2-1 `level rampup1`
### 2-2 `level rampup2`
### 2-3 `level rampup3`
- `git checkout HEAD~4`
- `git branch -f master HEAD~3`
```
git branch -f master C6
git checkout HEAD^
git branch -f bugFix HEAD~1
```

### 2-4 `level rampup4`
- `git reset HEAD~1`: local
- `git revert HEAD`
```
git reset local^
git checkout pushed
git revert pushed
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
git rebase -i HEAD~4
# omit C2, change C4 and C5
```
### 4-1 `level mixed1`
- `git cherry-pick`
- `git rebase -i`
```
git checkout master
git cherry-pick C4
```
### 4-1 `level mixed1`
### 4-2 `level mixed2`
### 4-3 `level mixed3`
### 4-4 `level mixed4`
### 4-5 `level mixed5`
### 5-1
### 5-2
### 5-3
