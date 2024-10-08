from django.apps import AppConfig
from django.conf import settings


class TwoFactorConfig(AppConfig):
    name = 'two_factor'
    verbose_name = "Django Two Factor Authentication"

    def ready(self):
        # import the signals to register our own listeners
        from . import signals  # noqa

        if getattr(settings, 'TWO_FACTOR_PATCH_ADMIN', True):
            from .admin import patch_admin
            patch_admin()
