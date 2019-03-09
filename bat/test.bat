@echo off

:: 対話入力
set /p ANS="入力してください: "
echo ANS: %ANS%

:: 引数の分解
echo arg1   : %1
echo arg1~1 : %~1
echo arg1~f1: %~f1
echo arg1~d1: %~d1
echo arg1~p1: %~p1
echo arg1~n1: %~n1
echo arg1~x1: %~x1
echo arg1~a1: %~a1
echo arg1~t1: %~t1
echo arg1~z1: %~z1

:: 引数を調べる
echo.
echo 引数を調べる1
for %%f in (%*) do (
  echo %%f
)
echo.
echo 引数を調べる2
:loop
if "%~1" == "" goto end
echo %1
shift
goto loop

:end


:: Windows バッチファイルの引数とパス名要素分解、対話入力、文字列置換まとめ
:: https://qiita.com/hkuno/items/e7fedc20a61979aa6078
:: .bat（バッチファイル）のforコマンド解説。
:: https://qiita.com/sawa_tsuka/items/67be34bab1fdf3fb87f9
:: .bat（バッチファイル）のifコマンド解説。
:: https://qiita.com/sawa_tsuka/items/8edf3d3d33a0ae86cb5c
:: Windowsのバッチファイル中で日付をファイル名に使用する (1/2)
:: https://www.atmarkit.co.jp/ait/articles/0405/01/news002.html
