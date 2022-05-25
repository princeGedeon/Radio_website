from django.apps import AppConfig


class PostAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Post_app'
    def ready(self):
        import Post_app.signals
