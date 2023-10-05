from bee_twitter.repository.models.cosmos.app_hashtags import AppHashtags

example_data = {
    "id": 1,
    "dt_creation": "2023-10-05T10:00:00",
    "dt_update": "2023-10-05T10:30:00",
    "dt_expiration": "2023-12-31T23:59:59",
    "cod_status": 200,
    "hashtag": "exemplo_hashtag",
    "name": "Hashtag de Exemplo",
    "description": "Esta é uma hashtag de exemplo para fins de demonstração.",
    "qtd_news": 50,
    "qtd_posts": 100,
    "dt_last_mention": "2023-10-05T11:15:00"
}

app_hashtags_add = AppHashtags(
    id=example_data["id"],
    dt_creation=example_data["dt_creation"],
    dt_update=example_data["dt_update"],
    dt_expiration=example_data["dt_expiration"],
    cod_status=example_data["cod_status"],
    hashtag=example_data["hashtag"],
    name=example_data["name"],
    description=example_data["description"],
    qtd_news=example_data["qtd_news"],
    qtd_posts=example_data["qtd_posts"],
    dt_last_mention=example_data["dt_last_mention"]
)

if __name__ == "__main__":
    print(app_hashtags_add)
