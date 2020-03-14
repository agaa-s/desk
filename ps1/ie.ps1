<# カレント・フォルダのパスから末尾の要素のみを抽出
function prompt() {
  Write-Host (Split-Path (Get-Location) -Leaf) -NoNewLine -ForegroundColor "Red"
  return "> "
}
#>

<# 参考
●VBAでインターネット上のファイルをダウンロードする方
https://www.ka-net.org/blog/?p=4855#HttpRequest
# XMLHTTPRequest
Set req = CreateObject("Msxml2.XMLHTTP") 
# WinHttpRequest
Set req = CreateObject("WinHttp.WinHttpRequest.5.1")
# HttpClient .NET CoreではHttpClientFactory

●PowerShell Scripting Weblog
http://winscript.jp/powershell/306 279 304 305

●tsl12
https://hi-matic.org/diary/?201901
if (-not ([Net.ServicePointManager]::SecurityProtocol -band [Net.SecurityProtocolType]::Tls12)) {
    [Net.ServicePointManager]::SecurityProtocol = [Net.ServicePointManager]::SecurityProtocol -bor [Net.SecurityProtocolType]::Tls12
}

#>
function ieTerminate($ie) {
    $ie.Quit()
    $ie = $null
    [GC]::Collect()
}

function ieWait($ie){
    while ($ie.busy -or $ie.readystate -ne 4) {
        Start-Sleep -Milliseconds 100
    }
}

function OverrideMethod ([mshtml.HTMLDocumentClass]$Document) {
    $doc = $Document | Add-Member -MemberType ScriptMethod -Name "gei" -Value {
        param($Id)
        [System.__ComObject].InvokeMember(
            "getElementById",
            [System.Reflection.BindingFlags]::InvokeMethod,
            $null,
            $this,
            $Id
        ) | Where-Object {$_ -ne [System.DBNull]::Value}
    } -Force -PassThru

    $doc | Add-Member -MemberType ScriptMethod -Name "gec" -Value {
        param($ClassName)
        [System.__ComObject].InvokeMember(
            "getElementsByClassName",
            [System.Reflection.BindingFlags]::InvokeMethod,
            $null,
            $this,
            $ClassName
        ) | Where-Object  {$_ -ne [System.DBNull]::Value}
    } -Force

    $doc | Add-Member -MemberType ScriptMethod -Name "gen" -Value {
        param($ClassName)
        [System.__ComObject].InvokeMember(
            "getElementsByName",
            [System.Reflection.BindingFlags]::InvokeMethod,
            $null,
            $this,
            $ClassName
        ) | Where-Object  {$_ -ne [System.DBNull]::Value}
    } -Force

    $doc | Add-Member -MemberType ScriptMethod -Name "get" -Value {
        param($TagName)
        [System.__ComObject].InvokeMember(
            "getElementsByTagName",
            [System.Reflection.BindingFlags]::InvokeMethod,
            $null,
            $this,
            $TagName
        ) | Where-Object  {$_ -ne [System.DBNull]::Value}
    } -Force

    $doc | Add-Member -MemberType ScriptMethod -Name "qs" -Value {
        param($Selector)
        [System.__ComObject].InvokeMember(
            "querySelector",
            [System.Reflection.BindingFlags]::InvokeMethod,
            $null,
            $this,
            $Selector
        ) | Where-Object  {$_ -ne [System.DBNull]::Value}
    } -Force

    $doc | Add-Member -MemberType ScriptMethod -Name "qsa" -Value {
        param($Selector)
        $nodes = [System.__ComObject].InvokeMember(
            "querySelectorAll",
            [System.Reflection.BindingFlags]::InvokeMethod,
            $null,
            $this,
            $Selector
        )
        $result = New-Object System.Collections.Generic.List[System.__ComObject]
        for($i = 0; $i -lt $nodes.Length; $i++){
            $result.Add(
                [System.__ComObject].InvokeMember(
                    "item",
                    [System.Reflection.BindingFlags]::InvokeMethod,
                    $null,
                    $nodes,
                    $i
                )
            )
        }
        $result
    } -Force

    return $doc
}   

$url = "http://www.google.com"

# シェルを取得
$shell = New-Object -ComObject Shell.Application

# IE起動
$ie = New-Object -ComObject InternetExplorer.Application

# 可視化
$ie.Visible = $true

# HWNDを記憶
$hwnd = $ie.HWND

# URLオープン(キャッシュ無効)
$ie.Navigate($url, 4)
ieWait($ie)

# IE再取得
while ($ie.Document -isnot [mshtml.HTMLDocumentClass]) {
    $ie = $shell.Windows() | Where-Object  {$_.HWND -eq $hwnd}
}

$doc = $ie.Document
$d = OverrideMethod($ie.Document)
