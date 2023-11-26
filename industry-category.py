### 業種の説明文を追加した CSVファイルを作成する Module ###

# 1. 業種分類の DataFlame を作成する

# 2. DataFrame から 業種の Recode を1つ1つ取得する & ChatGPTで、説明を作成する

# 3. 業種説明の Column を DataFlame に追加する

# 4. DataFlame を CSV に変換して Export する

######################################################################## 

## Import Block ##
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage, # システムメッセージ 
    HumanMessage, # 人間の質問 
)
import pprint
import os

import pandas as pd

# OpenAI API Key を Setする
openai_api_key=''

# 業種の説明文を作成する Func
def create_industry_description(industry_category) :

  # ChatGPTのキャラ設定
  chara_setting = f'''
  あなたは、日本の会社の業種について詳しいChatBotです。
  以下の制約条件を厳密に守ってロールプレイを行ってください。 

  制約条件: 
  * あなたは、日本の会社の業種について詳しいプロです。
  * あなたは投げかけられた質問に日本語で答える必要があります。
  '''

  # 質問文
  question = f'''{industry_category}とは、どんな業種ですか？'''
    
  ## ChatGPT・Instance ##
  llm = ChatOpenAI(
      openai_api_key=openai_api_key,
      model="gpt-4",
      temperature=0, # 精度を最大化する 
  )

  # LLM に渡すための Messageを作成する
  messages = [
      SystemMessage(content=chara_setting), # System Message = AIの「キャラ設定」のようなもの 
      HumanMessage(content=question) # 提案する内容 
  ]

  response = llm(messages)
  print(response)

  return {
    'result_msg': response.content,
  }

csv_file = '業種分類.csv'

csv_file_path = f'{os.getcwd()}/{csv_file}'

# 1. 業種分類の DataFlame
industry_category_df = pd.read_csv(csv_file_path, encoding="utf-8")

pprint.pprint(industry_category_df)

# 業種の説明文を格納するリスト
description_list = []

# 2. DataFrame から 業種の Recode を1つ1つ取得する & ChatGPTで、説明を作成する
for industry_category in industry_category_df['業種']:
    print(industry_category)
    result = create_industry_description(industry_category)
    description_list.append(result['result_msg'])


print('description_list')
print(description_list)

# 3. 業種説明の Column を DataFlame に追加する
industry_category_df['業種説明'] = description_list


new_csv_file = '業種分類(説明付き).csv'
create_csv_file_path = f'{os.getcwd()}/{new_csv_file}'

# 4. DataFlame を CSV に変換して Export する
industry_category_df.to_csv(create_csv_file_path, index = None, header=True)



