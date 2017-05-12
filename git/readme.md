# GitShell覚え書き

## 基本的なこと

clone
`git clone https://github.com/[ユーザ名]/[リポジトリ名]`

branch作成
`git checkout -b [Branchname]`

branch変更
`git checkout [BranchName]`

## PullRequests
```
git add .
git commit -m "[コメント]"
git push https://github.com/[ユーザ名]/[リポジトリ名] [BranchName]
```

## Fork元とリモートリポジトリの差分更新
```
git config --global url."https://".insteadOf git://
git remote add upstream git://github.com/[ユーザ名]/[リポジトリ名].git
git fetch upstream
git merge upstream/master
git push
git remote rm upstream
```
