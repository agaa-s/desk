#!/usr/bin/zsh

# bash シェルスクリプト入門 -シェルスクリプトのいろは
# https://shellscript.sunone.me/tutorial.html

# Ｂシェルスクリプト基礎文法最速マスター
# http://chaichan.lolipop.jp/src/BSH.htm

# ファイルやディレクトリが存在するかシェルスクリプトで確認する
# https://hacknote.jp/archives/31390/

# シェルコマンド1行で複数コマンドや条件に応じた実行をする
# https://qiita.com/wwwaltz/items/9ee247ee8fe3ab63fd27

# chmod u+x test.sh
# export PATH="${PATH}:."

while :
do
  echo ""
  echo "1: NDSDevelop"
  echo "2: NDSTrial"
  echo "3: NDS"
  echo "q: 終了"
  echo "選択してください."
  read aplId
  if [ "$aplId" = "1" ]; then
    aplName="NDSDevelop"
    break
  elif [ "$aplId" = "2" ]; then
    aplName="NDSTrial"
    break
  elif [ "$aplId" = "3" ]; then
    aplName="NDS"
    break
  elif [ "$aplId" = "q" -o "$aplId" = "Q" ]; then
    exit 0
  fi
done

targetDir="/usr/local/bin/tomcat/webapp/"
sourceDir="./"

# デプロイするフォルダの有無を確認する
if [ ! -d ${sourceDir}${aplName} ]; then
  echo "${sourceDir}${aplName} を準備してください."
  exit 1
fi

# tomcatサービスを停止
bash ./teststop.sh || (echo "tomcatを停止できませんでした" &&  exit 1)

# 現在のアプリケーションフォルダをバックアップする
echo ""
echo "${targetDir}${aplName} をバックアップします."
echo "何かキーを押してください."
read confirm
# TODO: tar を実行する
backupFile=${sourceDir}${aplName}"_$(date +%Y%m%d_%H%M%S).bak"
echo "tar cvzf ${backupFile} ${targetDir}${aplName}"
echo "${backupFile} を作成しました."

# 現在のアプリケーションフォルダを削除する
echo ""
echo "${targetDir}${aplName} を削除します."
echo "何かキーを押してください."
read confirm
# TODO: rm を実行する
echo "rm -rf ${targetDir}${aplName}"

# デプロイする
echo ""
echo "${sourceDir}${aplName} を ${targetDir} にコピーします."
echo "何かキーを押してください."
read confirm
# TODO: cp を実行する
echo "cp ${sourceDir}${aplName} ${targetDir}"

# tomcatサービスを起動
bash ./teststart.sh || (echo "tomcatを起動できませんでした" &&  exit 1)

exit 0
