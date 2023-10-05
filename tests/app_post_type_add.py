from bee_twitter.repository.models.cosmos.app_post_type import AppPostType

example_data = {
    "id": 1,
    "dt_creation": "2023-10-05T10:00:00",
    "dt_update": "2023-10-05T10:30:00",
    "dt_expiration": "2023-12-31T23:59:59",
    "cod_status": 200,
    "name": "Tipo de Post Exemplo",
    "description": "Este é um tipo de post de exemplo para fins de demonstração."
}

app_post_type_add = AppPostType(
    id=example_data["id"],
    dt_creation=example_data["dt_creation"],
    dt_update=example_data["dt_update"],
    dt_expiration=example_data["dt_expiration"],
    cod_status=example_data["cod_status"],
    name=example_data["name"],
    description=example_data["description"]
)

if __name__ == "__main__":
    print(app_post_type_add)
