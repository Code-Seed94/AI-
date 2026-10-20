# Git 브랜치 작업 흐름

| 내용 |
|---|
| `main` |
| ↓ |
| `main pull` |
| ↓ |
| `SourceTree: Stage > Commit > Push` |
| ↓ |
| `GitHub Pull Request`<br>`(base: main < compare: feature/login)` |
| ↓ |
| `Merge` |
| ↓ |
| `main pull` |

## Git 명령어

| Git 명령어 |
|---|
| `git branch` |
| `git status` |
| `git switch main` |
| `git pull origin main` |
| `git switch -c feature/login` |
| `git switch feature/login` |
| `git branch -d feature/login` |
