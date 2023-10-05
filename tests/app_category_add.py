from bee_twitter.repository.models.cosmos.app_category import AppCategory

example_data = {
    "id": 1,
    "dt_creation": "2023-10-05T10:00:00",
    "dt_update": "2023-10-05T10:30:00",
    "dt_expiration": "2023-12-31T23:59:59",
    "cod_status": 200,
    "hashtag": "exemplo_hashtag",
    "order": 1,
    "name": "Categoria de Exemplo",
    "description": "Esta é uma categoria de exemplo para fins de demonstração.",
    "img_small_url": "https://exemplo.com/imagem_pequena.jpg",
    "img_original_url": "https://exemplo.com/imagem_original.jpg"
}

app_category_add = AppCategory(
    id=example_data["id"],
    dt_creation=example_data["dt_creation"],
    dt_update=example_data["dt_update"],
    dt_expiration=example_data["dt_expiration"],
    cod_status=example_data["cod_status"],
    hashtag=example_data["hashtag"],
    order=example_data["order"],
    name=example_data["name"],
    description=example_data["description"],
    img_small_url=example_data["img_small_url"],
    img_original_url=example_data["img_original_url"]
)

if __name__ == "__main__":
    print(app_category_add)
