# Git Keyword Terminal

VS Code 통합 터미널에서 키워드로 Git 작업을 실행하는 로컬 확장입니다.

## 실행 방법

1. VS Code에서 이 저장소를 엽니다.
2. `F5`를 눌러 **Run Git Keyword Terminal Extension**을 실행합니다.
3. 명령 팔레트(`Ctrl+Shift+P`)에서 `Git Keyword Terminal: 키워드 실행`을 선택합니다.
4. `확인`, `풀`, `업뎃`, `키업`, `저장소 추가`, `저장소 삭제`, `머지`, `변경` 중 하나를 입력합니다.

명령이 실행되면 `Git Keyword Terminal`이라는 VS Code 통합 터미널에 결과가 표시됩니다.

`변경`은 워크스페이스의 [git-keywords.json](../git-keywords.json)을 열어 키워드 내용을 수정합니다.

대화형 에이전트와 연결하려면 확장 개발 호스트를 실행한 상태에서 워크스페이스의
`.vscode/git-keyword-request.json` 파일에 다음 형식으로 요청을 저장합니다. 확장이 파일을
감지하면 파일을 삭제하고 키워드를 통합 터미널에서 실행합니다.

```json
{
  "keyword": "확인"
}
```

## 주의사항

- `업뎃`은 모든 변경사항을 스테이징한 뒤 커밋 메시지를 묻고 push합니다.
- `풀`, `저장소 삭제`, `머지`는 통합 터미널에서 추가 확인을 받습니다.
- `저장소 추가`와 `저장소 삭제`는 GitHub 저장소 자체가 아니라 로컬 Git의 원격(remote)을 관리합니다.
