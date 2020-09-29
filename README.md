# 概要

## salesforce接続
simple_salesforceを利用。
使いやすいように、認証処理やリトライ処理をライブラリに。

lib_mt_salesforce.py
lib_mt_salesforce_settings.py
(.envから設定値を取る)
認証情報はaccess_objectに保存。

## リクエスト実行部
get...post...の処理は上記ライブラリを使ってsalesforceにリクエストする処理。SalesForce側のエンドポイントやSOQLが異なれば基本的には別ファイルとしている。
例外として、get_sobject.pyはObject名とIDを指定することでエンドポイントにアクセスする想定。

## 他
util.pyは共通処理があったら追加していく。
test_soqlは単純にsoqlをテストする用のファイル。本番では不要。
