from bee_twitter.repository.models.cosmos import AppAuthorQuality

example_data = {
    "id": 1,
    "dt_creation": "2023-10-05T10:00:00",
    "dt_update": "2023-10-05T10:30:00",
    "dt_expiration": "2023-12-31T23:59:59",
    "cod_status": 200,
    "id_publisher": 101,
    "id_author": 501,
    "name": "Autor de Exemplo",
    "twitter_profile": "https://twitter.com/exemplo",
    "author_description": "Este é um autor de exemplo para fins de demonstração.",
    "dt_last_mention": "2023-10-05T11:15:00",
    "img_small_url": "https://exemplo.com/imagem_pequena.jpg",
    "img_original_url": "https://exemplo.com/imagem_original.jpg",
    "num_votes": 100,
    "quality_result": "Aprovado",
    "quality_value": 0.95,
    "quality_description": "Este autor tem uma alta qualidade.",
    "quality_results": [
        {"category": "Relevância", "score": 9},
        {"category": "Originalidade", "score": 95},
        {"category": "Engajamento", "score": 92}
    ]
}

quality_results = []
for index, item in enumerate(example_data["quality_results"]):
    quality_results.append(
        {
            "order": index + 1,
            "name": item["category"],
            "quality_value": item["score"]
        }
    )

app_author_quality_add = AppAuthorQuality(
    id=example_data["id"],
    dt_creation=example_data["dt_creation"],
    dt_update=example_data["dt_update"],
    dt_expiration=example_data["dt_expiration"],
    cod_status=example_data["cod_status"],
    id_publisher=example_data["id_publisher"],
    id_author=example_data["id_author"],
    name=example_data["name"],
    twitter_profile=example_data["twitter_profile"],
    author_description=example_data["author_description"],
    dt_last_mention=example_data["dt_last_mention"],
    img_small_url=example_data["img_small_url"],
    img_original_url=example_data["img_original_url"],
    num_vote=example_data["num_votes"],
    quality_result=example_data["quality_result"],
    quality_value=example_data["quality_value"],
    quality_description=example_data["quality_description"],
    quality_results=quality_results
)

if __name__ == "__main__":
    print(app_author_quality_add)
