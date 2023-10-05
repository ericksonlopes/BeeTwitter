from bee_twitter.repository.models.cosmos.app_publisher import AppPublisher

example_data = {
    "id": 1,
    "dt_creation": "2023-10-05T10:00:00",
    "dt_update": "2023-10-05T10:30:00",
    "dt_expiration": "2023-12-31T23:59:59",
    "cod_status": 200,
    "hashtag": "exemplo_hashtag",
    "name": "Editora de Exemplo",
    "site_url": "https://exemplo.com",
    "publisher_icon": "https://exemplo.com/icon.png",
    "publisher_icon_small": "https://exemplo.com/icon_pequeno.png",
    "twitter_profile": "https://twitter.com/exemplo_editora",
    "dt_last_mention": "2023-10-05T11:15:00"
}

app_publisher_add = AppPublisher(
    id=example_data["id"],
    dt_creation=example_data["dt_creation"],
    dt_update=example_data["dt_update"],
    dt_expiration=example_data["dt_expiration"],
    cod_status=example_data["cod_status"],
    hashtag=example_data["hashtag"],
    name=example_data["name"],
    site_url=example_data["site_url"],
    publisher_icon=example_data["publisher_icon"],
    publisher_icon_small=example_data["publisher_icon_small"],
    twitter_profile=example_data["twitter_profile"],
    dt_last_mention=example_data["dt_last_mention"]
)

if __name__ == "__main__":
    print(app_publisher_add)
