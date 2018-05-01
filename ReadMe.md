﻿# このソフトウェアについて

GitHub簡易アップローダ。

* [Shell.Github.Commiter.20180316160244](https://github.com/ytyaru0/Shell.Github.Commiter.20180316160244)のスタンドアロン版
* [Shell.Github.Commiter.20180427171306](https://github.com/ytyaru0/Shell.Github.Commiter.20180427171306)のセキュリティ向上版

## 変更点

* 脱外部依存
    * sqlite3とそのDBへの依存を解消してテキストファイル保存にした

## 環境用コード

* 環境対応
    * Bash
    * Bash+SQLite3
    * Python
        * 3.6以降(f'':OK)
        * 3.4以降(pathlib:OK)
        * 2.7以降
    * Bash+Python
    * Bash+Python+SQLite3

環境を用意するのがハードルになってしまう。できるだけ簡素な環境が好ましい。

## 未実装の欲しい機能

* 入力の簡略化
    * 新規GitHubアカウントを登録するときはTSVファイルに書き込むだけ
        * Username, E-MailAddress, Password
        * 入力後の初回起動時、AccessTokenを自動取得する
            * トークンをTSVファイルに記録する
            * TSVのパスワードを`*`にする
* Github二要素認証対応

# 使い方

## 準備

Accounts.tsv
```
Username,MailAddress,Password
Username,MailAddress,Password
Username,MailAddress,Password
```

ファイルから丸見えなのでセキュリティ的に危険。だが、簡単に編集できる。

## 実行

```sh
$ push
```
```sh
$ push some_username
```

* `push`ファイルを環境変数`PATH`が通っている所に配置する。
* カレントディレクトリをリポジトリと想定する

## 確認表示

### JSON

[リモートリポジトリ生成API](https://developer.github.com/v3/repos/#create)の応答。何か変わっても知れるように。（デバッグ）

### ReadMe

```sh
カレントディレクトリに ReadMe.md が存在しません。作成してください。
```

間違ってカレントディレクトリが`/`などだった場合も、少しは安心。

### User

```sh
ユーザを選択してください。
1) user1  3) user3  5) user5
2) user2  4) user4  6) user6
```

起動引数がなければ、CSVから全ユーザ名を取得して選択肢を出す。辞書順。

```sh
指定されたユーザ名はDBに登録されていません。
```

起動引数でユーザ名を指定しても、DBになければエラーになる。

### add前

* `git status -s`
* `git add -n .`

`git status`を追加。`git rm some.py`などで削除だけしたときも変化がわかるようにした。

### push出力

`git push`コマンドがstderrにパスワードを含むURLを出していたのを抑制した。

```sh
To https://{user}:{pass}@github.com/{user}/{repo}.git
```

# 開発環境

* [Raspberry Pi](https://ja.wikipedia.org/wiki/Raspberry_Pi) 3 Model B
    * [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) GNU/Linux 8.0 (jessie)
        * bash 4.3.30

# ライセンス

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

利用ライブラリは以下。

Library|License|Copyright
-------|-------|---------
[assert.sh](https://github.com/lehmannro/assert.sh)|[LGPL-3.0](https://github.com/lehmannro/assert.sh/blob/master/COPYING.LESSER)|[Copyright (C) 2007 Free Software Foundation, Inc. http://fsf.org/](https://github.com/lehmannro/assert.sh/blob/master/COPYING)

