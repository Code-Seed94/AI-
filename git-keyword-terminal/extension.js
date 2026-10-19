const vscode = require("vscode");
const fs = require("fs");
const path = require("path");

function quotePowerShell(value) {
  return `'${String(value).replace(/'/g, "''")}'`;
}

function getWorkspaceFolder() {
  return vscode.workspace.workspaceFolders?.[0];
}

function getTerminal(workspaceFolder) {
  const terminalName = vscode.workspace
    .getConfiguration("gitKeywordTerminal")
    .get("terminalName", "Git Keyword Terminal");
  let terminal = vscode.window.terminals.find(
    (item) => item.name === terminalName,
  );
  if (!terminal) {
    terminal = vscode.window.createTerminal({
      name: terminalName,
      cwd: workspaceFolder.uri.fsPath,
    });
  }
  return terminal;
}

async function executeKeyword(context, workspaceFolder, keyword) {
  if (keyword === "변경") {
    await vscode.commands.executeCommand("gitKeywordTerminal.openConfig");
    return;
  }

  const terminal = getTerminal(workspaceFolder);
  terminal.show(true);
  const scriptPath = path.join(context.extensionPath, "git-keyword.ps1");
  const command = [
    "&",
    quotePowerShell(scriptPath),
    "-Keyword",
    quotePowerShell(keyword.trim()),
    "-WorkspacePath",
    quotePowerShell(workspaceFolder.uri.fsPath),
  ].join(" ");
  terminal.sendText(command, true);
}

async function processRequestFile(context, workspaceFolder) {
  const requestPath = path.join(
    workspaceFolder.uri.fsPath,
    ".vscode",
    "git-keyword-request.json",
  );
  try {
    const request = JSON.parse(await fs.promises.readFile(requestPath, "utf8"));
    const keyword = String(request.keyword || "").trim();
    if (!keyword) {
      throw new Error("요청 파일에 keyword가 없습니다.");
    }
    await executeKeyword(context, workspaceFolder, keyword);
  } catch (error) {
    vscode.window.showErrorMessage(`Git 키워드 요청을 실행하지 못했습니다: ${error.message}`);
  } finally {
    try {
      await fs.promises.unlink(requestPath);
    } catch (error) {
      if (error.code !== "ENOENT") {
        vscode.window.showWarningMessage(`요청 파일을 정리하지 못했습니다: ${error.message}`);
      }
    }
  }
}

function activate(context) {
  const runKeyword = vscode.commands.registerCommand(
    "gitKeywordTerminal.runKeyword",
    async () => {
      const workspaceFolder = getWorkspaceFolder();
      if (!workspaceFolder) {
        vscode.window.showErrorMessage("먼저 Git 저장소 폴더를 VS Code에서 열어주세요.");
        return;
      }

      const keyword = await vscode.window.showInputBox({
        prompt: "실행할 Git 키워드를 입력하세요.",
        placeHolder: "확인, 풀, 업뎃, 키업, 저장소 추가, 저장소 삭제, 머지, 변경",
        ignoreFocusOut: true,
      });

      if (keyword?.trim()) {
        await executeKeyword(context, workspaceFolder, keyword.trim());
      }
    },
  );

  const openConfig = vscode.commands.registerCommand(
    "gitKeywordTerminal.openConfig",
    async () => {
      const workspaceFolder = getWorkspaceFolder();
      if (!workspaceFolder) {
        vscode.window.showErrorMessage("먼저 Git 저장소 폴더를 VS Code에서 열어주세요.");
        return;
      }
      const configUri = vscode.Uri.joinPath(
        workspaceFolder.uri,
        "git-keywords.json",
      );
      const document = await vscode.workspace.openTextDocument(configUri);
      await vscode.window.showTextDocument(document);
    },
  );

  const workspaceFolder = getWorkspaceFolder();
  const subscriptions = [runKeyword, openConfig];
  if (workspaceFolder) {
    const watcher = vscode.workspace.createFileSystemWatcher(
      new vscode.RelativePattern(workspaceFolder, ".vscode/git-keyword-request.json"),
    );
    let processing = false;
    const process = async () => {
      if (processing) {
        return;
      }
      processing = true;
      try {
        await processRequestFile(context, workspaceFolder);
      } finally {
        processing = false;
      }
    };
    subscriptions.push(
      watcher,
      watcher.onDidCreate(process),
      watcher.onDidChange(process),
    );
  }
  context.subscriptions.push(...subscriptions);
}

function deactivate() {}

module.exports = { activate, deactivate };
