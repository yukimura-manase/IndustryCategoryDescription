# 業種の説明文を追加した CSVファイルを作成する Module

1. 業種の説明文を追加した 業種分類(説明付き)CSVファイルを作成する Module

## 前提条件

1. Python環境構築済みであること。

2. 内部に、業種分類のCSVファイルを配置すること。

3. OpenAI の API Key を取得して、Setすること。

## 処理内容

1. 業種分類の DataFlame を作成する

2. DataFrame から 業種の Recode を1つ1つ取得する & ChatGPTで、説明を作成する

3. 業種説明の Column を DataFlame に追加する

4. DataFlame を CSV に変換して Export する
