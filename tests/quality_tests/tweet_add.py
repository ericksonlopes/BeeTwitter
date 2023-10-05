from datetime import datetime

import pandas as pd


def tweet_adding_function(data, quality_data, tweet_data_list):
    for i in range(len(quality_data["quality_results_name"])):
        new_tweet = dict(
            id=data["id"][0],
            id_tweet=data["id_tweet"][0],
            text=data["text"][0],
            tweet_text=data["tweet_text"][0],
            dt_creation=data["dt_creation"][0],
            dt_update=data["dt_update"][0],
            dt_expiration=data["dt_expiration"][0],
            url=data["url"][0],
            author_id=data["author_id"][0],
            quality_results_name=quality_data["quality_results_name"][i],  # Correção aqui
            quality_results_value=quality_data["quality_results_value"][i]  # Correção aqui
        )
        tweet_data_list.append(new_tweet)
    return tweet_data_list


tweet_list = []

data1 = {
    "id": [1],
    "id_tweet": ["123456"],
    "text": ["Texto 1"],
    "tweet_text": ["Tweet 1"],
    "dt_creation": [datetime(2023, 10, 5, 10, 0)],
    "dt_update": [datetime(2023, 10, 7, 12, 30)],
    "dt_expiration": [datetime(2023, 12, 31, 23, 59, 59)],
    "url": ["https://example.com/1"],
    "author_id": [101],
}
quality_data1 = {
    "quality_results_name": ["Relevância", "Originalidade", "Geral"],
    "quality_results_value": [90, 95, 92]
}

data2 = {
    "id": [2],
    "id_tweet": ["789012"],
    "text": ["Texto 2"],
    "tweet_text": ["Tweet 2"],
    "dt_creation": [datetime(2023, 10, 6, 11, 0)],
    "dt_update": [datetime(2023, 10, 5, 10, 30)],
    "dt_expiration": [datetime(2023, 12, 31, 23, 59, 59)],
    "url": ["https://example.com/2"],
    "author_id": [101],
}
quality_data2 = {
    "quality_results_name": ["Relevância", "Originalidade", "Geral"],
    "quality_results_value": [88, 93, 89]
}

tweet_adding_function(data1, quality_data1, tweet_list)
tweet_adding_function(data2, quality_data2, tweet_list)

df = pd.DataFrame(tweet_list)
df2 = df.groupby('quality_results_name')['quality_results_value'].mean().reset_index()

dicionario = df2.to_dict()

if __name__ == "__main__":
    print(dicionario)
