param(
    [Parameter(Mandatory = $true)]
    [string]$Keyword,

    [Parameter(Mandatory = $true)]
    [string]$WorkspacePath
)

$ErrorActionPreference = "Stop"

function Invoke-Git {
    param([Parameter(ValueFromRemainingArguments = $true)][string[]]$Arguments)
    & git @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "git 명령이 실패했습니다: git $($Arguments -join ' ')"
    }
}

function Read-Confirmation {
    param([string]$Message)
    $answer = Read-Host "$Message (y/N)"
    return $answer -match "^(y|yes|예|ㅇ)$"
}

function Get-CurrentBranch {
    return (git branch --show-current).Trim()
}

Set-Location -LiteralPath $WorkspacePath
$branch = Get-CurrentBranch

Write-Host "`n[Git Keyword Terminal] $Keyword" -ForegroundColor Cyan
Write-Host "저장소: $(Get-Location)"
Write-Host "브랜치: $branch`n"

switch ($Keyword) {
    "확인" {
        Write-Host "[원격 변경사항 확인]" -ForegroundColor Yellow
        Invoke-Git fetch origin
        git status --short --branch
        Write-Host "`n[로컬과 origin/$branch 커밋 차이]"
        git rev-list --left-right --count "HEAD...origin/$branch"
        Write-Host "`n[원격에만 있는 커밋]"
        git log --oneline "HEAD..origin/$branch"
        Write-Host "`n[원격 변경 내용]"
        git diff --stat "HEAD..origin/$branch"
        git diff "HEAD..origin/$branch"
        break
    }

    "풀" {
        Invoke-Git fetch origin
        $dirty = @(git status --porcelain)
        if ($dirty.Count -gt 0) {
            Write-Host "변경된 로컬 내용이 있습니다:" -ForegroundColor Yellow
            $dirty
            if (-not (Read-Confirmation "변경사항을 확인했습니까? 계속 pull 하시겠습니까?")) {
                Write-Host "pull을 취소했습니다."
                break
            }
        }
        Invoke-Git pull --ff-only origin $branch
        break
    }

    "업뎃" {
        git add --all
        $staged = @(git diff --cached --name-only)
        if ($staged.Count -eq 0) {
            Write-Host "커밋할 변경사항이 없습니다."
            break
        }
        Write-Host "커밋 대상 파일:" -ForegroundColor Yellow
        $staged
        $message = "업뎃: $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
        Write-Host "자동 커밋 메시지: $message"
        Invoke-Git commit -m $message
        Invoke-Git push origin $branch
        break
    }

    "저장소 추가" {
        Write-Host "현재 원격 저장소:" -ForegroundColor Yellow
        git remote -v
        $name = Read-Host "추가할 원격 저장소 이름"
        $url = Read-Host "추가할 원격 저장소 URL"
        if ([string]::IsNullOrWhiteSpace($name) -or [string]::IsNullOrWhiteSpace($url)) {
            Write-Host "저장소 추가를 취소했습니다."
            break
        }
        if (Read-Confirmation "'$name' 저장소를 추가하시겠습니까?") {
            Invoke-Git remote add $name $url
            Write-Host "저장소를 추가했습니다."
            git remote -v
        }
        break
    }

    "저장소 삭제" {
        Write-Host "현재 원격 저장소:" -ForegroundColor Yellow
        git remote -v
        $name = Read-Host "삭제할 원격 저장소 이름"
        if ([string]::IsNullOrWhiteSpace($name)) {
            Write-Host "저장소 삭제를 취소했습니다."
            break
        }
        $dirty = @(git status --porcelain)
        if ($dirty.Count -gt 0) {
            Write-Host "삭제 전 확인: 로컬 변경사항이 있습니다." -ForegroundColor Yellow
            $dirty
        }
        $ahead = @(git rev-list --count "$name/$branch..HEAD" 2>$null)
        if (($dirty.Count -gt 0) -or (($ahead.Count -gt 0) -and ([int]$ahead[0] -gt 0))) {
            if (-not (Read-Confirmation "변경사항을 확인했습니까? '$name' 원격을 삭제하시겠습니까?")) {
                Write-Host "저장소 삭제를 취소했습니다."
                break
            }
        }
        Invoke-Git remote remove $name
        Write-Host "'$name' 원격 저장소를 삭제했습니다."
        break
    }

    "머지" {
        Write-Host "병합 가능한 브랜치:" -ForegroundColor Yellow
        git branch --all
        $source = Read-Host "병합할 브랜치 이름"
        if ([string]::IsNullOrWhiteSpace($source)) {
            Write-Host "머지를 취소했습니다."
            break
        }
        if (Read-Confirmation "'$source' 브랜치를 '$branch'에 병합하시겠습니까?") {
            Invoke-Git merge $source
        }
        break
    }

    "키업" {
        $configPath = Join-Path $PSScriptRoot "keywords.json"
        Write-Host "등록된 키워드:" -ForegroundColor Yellow
        Get-Content -LiteralPath $configPath -Raw
        break
    }

    default {
        Write-Host "알 수 없는 키워드입니다: $Keyword" -ForegroundColor Red
        Write-Host "지원 키워드: 업뎃, 확인, 풀, 키업, 변경, 저장소 추가, 저장소 삭제, 머지"
        break
    }
}
