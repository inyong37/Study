# [Git](https://git-scm.com/)

Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.

Git is easy to learn and has a tiny footprint with lightning fast performance. It outclasses SCM tools like Subversion, CVS, Perforce, and ClearCase with features like cheap local branching, convenient staging areas, and multiple workflows.

### [Github](https://github.com/)

GitHub is how people build software, it's supporting a community where more than 50 million people learn, share, and work together to build software. First commit was October 2007, headquarters is at San Francisco, and Repositories hosted about 100 million.

### [GitLab](https://about.gitlab.com/) | [GitHub](https://github.com/gitlabhq)

GitLab은 Git의 원격 저장소 기능과 이슈 트래커 기능 등을 제공하는 소프트웨어다. 설치형 GitHub라는 컨셉으로 시작된 프로젝트이기 때문에 GitHub와 비슷한 면이 많이 있다. 서비스형 원격저장소를 운영하는 것에 대한 비용이 부담되거나, 소스코드의 보안이 중요한 프로젝트에 적당하다. 설치형 버전관리 시스템으로 자신의 서버에 직접 설치해서 사용할 수 있다. 클라우드 버전 관리 시스템은 gitlab.com을 이용하면 서버 없이도 GitLab의 기능을 이용할 수 있다. 10명 이하의 프로젝트는 무료로 사용할 수 있다.

### [GitLab vs. GitHub](https://about.gitlab.com/competition/github/)

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

## hooks
Srcipts can use same shebang in Windows as UNIX.

```Python
#!/usr/bin/env python
```

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

Add Submodule:

- `git submodule add git@github.com:user_name/submodule_name path_name`

Delete Submodule:

1. `git submodule deinit -f submodule_name`
2. UNIX: `rm -rf .git/modules/submodule_name`
3. Windows: `rd /s /q .git/modules/submodule_name`
4. `git rm -f path_name/submodule_name`

### Subtree
main project에서 sub folder/project를 분리하는 방법이다.
1. Split sub project from main project: `cd mainproject_name && git subtree split -P subproject_name -b branch_name`
2. Make new folder/directory for sub porject: `cd workspace_name && mkdir subproject_name & cd subproject_name`
3. Git init subproject: `git init`
4. Git pull sub project from main project: `git pull mainproject_path branch_name`
5. Add git remote repository: `git remote add remote_name git_name`
6. Push sub project content: `git push remote_name -u branch_name`
7. Additionally remove sub project folder/directory in main project: `cd mainproject_name && git rm -r subproject_name`
8. Commit and push changes: `git commit -m "split subproject" && git push`

#### Submodule vs. Subtree
- Submodule은 main에서 sub의 SHA 값만 기록하기 때문에 main에서 수정한 sub folder의 내용은 사라지고 항상 submodule의 내용으로 업데이트된다. 따라서 항상 작업은 sub에서 한 뒤 이를 커밋하고 main에서 업데이트(`git submodule update subproject_name`) 해야 한다.
- Subtree는 submodule과 달리 main에 file/folder를 직접 추가하고 tracking한다. 따라서 sub의 변경 사항도 main에 기록되며, subtree의 remote의 content와 subtree를 추가한 repo(main)의 content가 서로 달라도 `subtree merge`를 사용하면 변경 사항을 양쪽 모두에 반영 가능하다.
- main에서 sub를 직접 수정하고 remote에 push할 수 있다는 점이 차이점이다. 즉, 자유도가 높다.
- 단, subtree를 추가한 모든 사용자가 subtree의 내용을 자유롭게 변경해서 remote에 push할 수 있기 떄문에 문제가 발생할 수 있다.

### Switch
git 2.23.0 부터 branch를 switch하기 위한 command이다. 이전의 checkout의 기능을 세분화한 것이다.
- `git switch branch_name` = `git checkout branch_name`

### Token
- How to setup GitHub token in config file
  - `git config --global github.token`

---

## [gitignore](https://github.com/github/gitignore/tree/main) | [Generator](https://www.toptal.com/developers/gitignore)

```Bash
.DS_Store
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/
.mypy_cache/
.dmypy.json
dmypy.json
.idea
.vscode
```

<details>
<summary>Windows</summary>
  
```Bash
# Created by https://www.toptal.com/developers/gitignore/api/windows
# Edit at https://www.toptal.com/developers/gitignore?templates=windows

### Windows ###
# Windows thumbnail cache files
Thumbs.db
Thumbs.db:encryptable
ehthumbs.db
ehthumbs_vista.db

# Dump file
*.stackdump

# Folder config file
[Dd]esktop.ini

# Recycle Bin used on file shares
$RECYCLE.BIN/

# Windows Installer files
*.cab
*.msi
*.msix
*.msm
*.msp

# Windows shortcuts
*.lnk

# End of https://www.toptal.com/developers/gitignore/api/windows
```

</details>

<details>
<summary>macOS</summary>

```Bash
# Created by https://www.toptal.com/developers/gitignore/api/macos
# Edit at https://www.toptal.com/developers/gitignore?templates=macos

### macOS ###
# General
.DS_Store
.AppleDouble
.LSOverride

# Icon must end with two \r
Icon


# Thumbnails
._*

# Files that might appear in the root of a volume
.DocumentRevisions-V100
.fseventsd
.Spotlight-V100
.TemporaryItems
.Trashes
.VolumeIcon.icns
.com.apple.timemachine.donotpresent

# Directories potentially created on remote AFP share
.AppleDB
.AppleDesktop
Network Trash Folder
Temporary Items
.apdisk

### macOS Patch ###
# iCloud generated files
*.icloud

# End of https://www.toptal.com/developers/gitignore/api/macos
```

</details>

<details>
<summary>Linux</summary>

```Bash
# Created by https://www.toptal.com/developers/gitignore/api/linux
# Edit at https://www.toptal.com/developers/gitignore?templates=linux

### Linux ###
*~

# temporary files which can be created if a process still has a handle open of a deleted file
.fuse_hidden*

# KDE directory preferences
.directory

# Linux trash folder which might appear on any partition or disk
.Trash-*

# .nfs files are created when an open file is removed but is still being accessed
.nfs*

# End of https://www.toptal.com/developers/gitignore/api/linux
```

</details>

<details>
<summary>Python</summary>

```Bash
# Created by https://www.toptal.com/developers/gitignore/api/python
# Edit at https://www.toptal.com/developers/gitignore?templates=python

### Python ###
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#pdm.lock
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/#use-with-ide
.pdm.toml

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/

### Python Patch ###
# Poetry local configuration file - https://python-poetry.org/docs/configuration/#local-configuration
poetry.toml

# ruff
.ruff_cache/

# LSP config files
pyrightconfig.json

# End of https://www.toptal.com/developers/gitignore/api/python
```

</details>

<details>
<summary>PyCharm</summary>

```Bash
# Created by https://www.toptal.com/developers/gitignore/api/pycharm
# Edit at https://www.toptal.com/developers/gitignore?templates=pycharm

### PyCharm ###
# Covers JetBrains IDEs: IntelliJ, RubyMine, PhpStorm, AppCode, PyCharm, CLion, Android Studio, WebStorm and Rider
# Reference: https://intellij-support.jetbrains.com/hc/en-us/articles/206544839

# User-specific stuff
.idea/**/workspace.xml
.idea/**/tasks.xml
.idea/**/usage.statistics.xml
.idea/**/dictionaries
.idea/**/shelf

# AWS User-specific
.idea/**/aws.xml

# Generated files
.idea/**/contentModel.xml

# Sensitive or high-churn files
.idea/**/dataSources/
.idea/**/dataSources.ids
.idea/**/dataSources.local.xml
.idea/**/sqlDataSources.xml
.idea/**/dynamic.xml
.idea/**/uiDesigner.xml
.idea/**/dbnavigator.xml

# Gradle
.idea/**/gradle.xml
.idea/**/libraries

# Gradle and Maven with auto-import
# When using Gradle or Maven with auto-import, you should exclude module files,
# since they will be recreated, and may cause churn.  Uncomment if using
# auto-import.
# .idea/artifacts
# .idea/compiler.xml
# .idea/jarRepositories.xml
# .idea/modules.xml
# .idea/*.iml
# .idea/modules
# *.iml
# *.ipr

# CMake
cmake-build-*/

# Mongo Explorer plugin
.idea/**/mongoSettings.xml

# File-based project format
*.iws

# IntelliJ
out/

# mpeltonen/sbt-idea plugin
.idea_modules/

# JIRA plugin
atlassian-ide-plugin.xml

# Cursive Clojure plugin
.idea/replstate.xml

# SonarLint plugin
.idea/sonarlint/

# Crashlytics plugin (for Android Studio and IntelliJ)
com_crashlytics_export_strings.xml
crashlytics.properties
crashlytics-build.properties
fabric.properties

# Editor-based Rest Client
.idea/httpRequests

# Android studio 3.1+ serialized cache file
.idea/caches/build_file_checksums.ser

### PyCharm Patch ###
# Comment Reason: https://github.com/joeblau/gitignore.io/issues/186#issuecomment-215987721

# *.iml
# modules.xml
# .idea/misc.xml
# *.ipr

# Sonarlint plugin
# https://plugins.jetbrains.com/plugin/7973-sonarlint
.idea/**/sonarlint/

# SonarQube Plugin
# https://plugins.jetbrains.com/plugin/7238-sonarqube-community-plugin
.idea/**/sonarIssues.xml

# Markdown Navigator plugin
# https://plugins.jetbrains.com/plugin/7896-markdown-navigator-enhanced
.idea/**/markdown-navigator.xml
.idea/**/markdown-navigator-enh.xml
.idea/**/markdown-navigator/

# Cache file creation bug
# See https://youtrack.jetbrains.com/issue/JBR-2257
.idea/$CACHE_FILE$

# CodeStream plugin
# https://plugins.jetbrains.com/plugin/12206-codestream
.idea/codestream.xml

# Azure Toolkit for IntelliJ plugin
# https://plugins.jetbrains.com/plugin/8053-azure-toolkit-for-intellij
.idea/**/azureSettings.xml

# End of https://www.toptal.com/developers/gitignore/api/pycharm
```

</details>

<details>
<summary>Visual Studio Code</summary>

```Bash
# Created by https://www.toptal.com/developers/gitignore/api/visualstudiocode
# Edit at https://www.toptal.com/developers/gitignore?templates=visualstudiocode

### VisualStudioCode ###
.vscode/*
!.vscode/settings.json
!.vscode/tasks.json
!.vscode/launch.json
!.vscode/extensions.json
!.vscode/*.code-snippets

# Local History for Visual Studio Code
.history/

# Built Visual Studio Code Extensions
*.vsix

### VisualStudioCode Patch ###
# Ignore all local history of files
.history
.ionide

# End of https://www.toptal.com/developers/gitignore/api/visualstudiocode
```

</details>

---

## [Git Tutorial Game](https://learngitbranching.js.org/)

<details>
<summary>Solution</summary>

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

</details>

---

### Reference
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
- git subtree Blog KR, https://yh0921k.tistory.com/27, 2020-01-20-Wed.
- git submodule vs. subtree Blog KR, https://blog.rhostem.com/posts/2020-01-03-code-sharing-with-git-subtree, 2020-01-20-Wed.
- git hook shebang in Windows Blog, https://skoop.dev/blog/2018/12/12/git_hooks_on_Windows/, 2021-05-28-Fri.
- GitLab vs. GitHub, https://about.gitlab.com/competition/github/, 2023-09-12-Tue.
- gitignore Generator, https://www.toptal.com/developers/gitignore, 2024-07-17-Wed.
