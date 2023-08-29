from src.services.api_v1_service import APITwitterV1Service

api = APITwitterV1Service()
print(api.get_user(screen_name='jairbolsonaro').__dict__["_json"])
