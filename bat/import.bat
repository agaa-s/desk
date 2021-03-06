@echo off

set $flg=.flg
set $csv=.bat

for %%f in (%*) do (  
  if exist %%f.flg (
    call .\logmsg.bat logfile %%f%$flg%が見つかりました
    notepad %%f%$csv%
    call .\logmsg.bat logfile %%f%$csv%のインポートを実行しました[%ERRORLEVEL%]
    del %%f.flg
  ) else (
    call .\logmsg.bat logfile %%f%$flg%が見つかりませんでした
  )
)
