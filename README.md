# desk
Created on 2018-12-29 from ubuntu 18.04
Add this line.
129c69ad9b35089cf36f3d6aacf4abbc8c8d5378
https://guides.github.com/activities/hello-world/#pr
https://github.com/agaa-s/desk

・git-controlエラー
https://github.com/jacogr/atom-git-control/issues/259

  At ~/.atom/packages/git-control/lib/git-control-view.coffee:76
  TypeError: Cannot read property 'split' of undefined

  if git.getRepository().path
   @setWorkspaceTitle(git.getRepository().path.split('/').reverse()[1])
  else
   @setWorkspaceTitle(git.getRepository().repo.workingDirectory.split('/').reverse()[0]


2019-01-12
[python3]
・pip3のインストール
・flaskのインストール
・pipのインストール先・・・ $ pip3 show flask

[atom]
・python-debuggerのインストール
  Settings python->python3
→vscodeにしようかな？
・GitHub Tab を出そうとすると No pull request could be found ... になり
　先に進めない・・・確か前回もそうだったような
・ただしatomからGitHubにpullはできることを確認した
