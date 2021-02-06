from django.apps import AppConfig


class PayConfig(AppConfig):
    name = 'pay'

    def ready(self):
        import pay.signal
