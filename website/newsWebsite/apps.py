from django.apps import AppConfig


class NewswebsiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'newsWebsite'

    class Meta:
        verbols_name = 'news'
