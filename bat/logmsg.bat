:: usage: logmsg ログファイル名 メッセージ

if "%~1" == "" goto end

:: 日付からログファイル名を整形
set $now=%date% %time%
set $logfile=%1%$now:~0,4%%$now:~5,2%.log

:: ログファイルに出力
echo %date% %time%  %2 >> %$logfile%

:end
