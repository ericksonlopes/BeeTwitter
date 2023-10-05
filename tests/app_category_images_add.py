from bee_twitter.repository.models.cosmos.app_category_images import AppCategoryImages

example_data = {
    "id": 1,
    "dt_creation": "2023-10-05T10:00:00",
    "dt_update": "2023-10-05T10:30:00",
    "dt_expiration": "2023-12-31T23:59:59",
    "cod_status": 200,
    "nom_file": "imagem_exemplo.png",
    "text_image": "Esta é uma imagem de exemplo.",
    "id_category": 101,
    "nom_category": "Categoria de Exemplo",
    "url_original": "https://exemplo.com/imagem_original.png",
    "url_large": "https://exemplo.com/imagem_grande.png",
    "url_small": "https://exemplo.com/imagem_pequena.png"
}

app_category_images_add = AppCategoryImages(
    id=example_data["id"],
    dt_creation=example_data["dt_creation"],
    dt_update=example_data["dt_update"],
    dt_expiration=example_data["dt_expiration"],
    cod_status=example_data["cod_status"],
    nom_file=example_data["nom_file"],
    text_image=example_data["text_image"],
    id_category=example_data["id_category"],
    nom_category=example_data["nom_category"],
    url_original=example_data["url_original"],
    url_large=example_data["url_large"],
    url_small=example_data["url_small"]
)

if __name__ == "__main__":
    print(app_category_images_add)
