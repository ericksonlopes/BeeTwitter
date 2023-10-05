from bee_twitter.repository.models.cosmos.app_news import AppNews

example_data = {
    "id": 1,
    "dt_creation": "2023-10-05T10:00:00",
    "dt_update": "2023-10-05T10:30:00",
    "dt_expiration": "2023-12-31T23:59:59",
    "cod_status": 200,
    "post_type": "Notícia",
    "friendly_url": "exemplo-noticia",
    "title": "Título da Notícia de Exemplo",
    "resume": "Este é um resumo da notícia de exemplo.",
    "content_demo": "Este é um conteúdo de demonstração para a notícia.",
    "content": "Este é o conteúdo completo da notícia de exemplo.",
    "text_ai_analysis": "A análise de AI conclui que esta notícia é relevante e informativa.",
    "img_small_url": "https://exemplo.com/imagem_pequena.jpg",
    "img_original_url": "https://exemplo.com/imagem_original.jpg",
    "publisher": "Editora de Exemplo",
    "category": [
        {"id_category": 101, "name_category": "Categoria de Exemplo 1"},
        {"id_category": 102, "name_category": "Categoria de Exemplo 2"}
    ],
    "author": [
        {"name_author": "Autor de Exemplo", "twitter_profile": "https://twitter.com/exemplo_autor"}
    ],
    "hashtags": "#noticia #exemplo #informacao",
    "num_vote": 100
}

app_news_add = AppNews(
    id=example_data["id"],
    dt_creation=example_data["dt_creation"],
    dt_update=example_data["dt_update"],
    dt_expiration=example_data["dt_expiration"],
    cod_status=example_data["cod_status"],
    post_type=example_data["post_type"],
    friendly_url=example_data["friendly_url"],
    title=example_data["title"],
    resume=example_data["resume"],
    content_demo=example_data["content_demo"],
    content=example_data["content"],
    text_ai_analysis=example_data["text_ai_analysis"],
    img_small_url=example_data["img_small_url"],
    img_original_url=example_data["img_original_url"],
    publisher=example_data["publisher"],
    category=example_data["category"],
    author=example_data["author"],
    hashtags=example_data["hashtags"],
    num_vote=example_data["num_vote"]
)

if __name__ == "__main__":
    print(app_news_add)
