from bee_twitter.repository.connect import Connector
from bee_twitter.repository.models.user_model import UserModel

from bee_twitter.services import APITwitterV1Service


class TwitterAPIV1Controller(APITwitterV1Service):

    def user(self, screen_name: str):
        try:
            data = self.get_user(screen_name=screen_name).__dict__["_json"]

            user = UserModel(
                id=data.get('id', None),
                id_str=data['id_str'],
                name=data['name'],
                screen_name=data['screen_name'],
                location=data['location'],
                description=data['description'],
                url=data['url'],
                protected=data['protected'],
                followers_count=data['followers_count'],
                friends_count=data['friends_count'],
                listed_count=data['listed_count'],
                created_at=data['created_at'],
                favourites_count=data['favourites_count'],
                verified=data['verified'],
                statuses_count=data['statuses_count'],
                lang=data['lang'],
                profile_image_url=data['profile_image_url'],
                profile_banner_url=data['profile_banner_url'],
                profile_link_color=data['profile_link_color'],
                profile_sidebar_fill_color=data['profile_sidebar_fill_color'],
                profile_text_color=data['profile_text_color'],
                has_extended_profile=data['has_extended_profile'],
                default_profile=data['default_profile'],
                default_profile_image=data['default_profile_image'],
                follow_request_sent=data['follow_request_sent'],
                notifications=data['notifications'],
                geo_enabled=data['geo_enabled'],
                time_zone=data['time_zone'],
                contributors_enabled=data['contributors_enabled'],
                is_translator=data['is_translator'],
                is_translation_enabled=data['is_translation_enabled'],
                profile_background_color=data['profile_background_color'],
                profile_background_image_url=data['profile_background_image_url'],
                profile_background_image_url_https=data['profile_background_image_url_https'],
                profile_background_tile=data['profile_background_tile'],
                profile_image_url_https=data['profile_image_url_https'],
                profile_sidebar_border_color=data['profile_sidebar_border_color'],
                profile_use_background_image=data['profile_use_background_image'],
                translator_type=data['translator_type']
            )

            with Connector() as session:
                session.add(user)

        except Exception as error:
            print(error)
            return False

        print(user.__dict__)
        return True


if __name__ == '__main__':
    api = TwitterAPIV1Controller()
    api.user(screen_name='jairbolsonaro')
