from django.apps import AppConfig


class RequesterConfig(AppConfig):
    name = 'requester'

    def ready(self):
        import requester.signals
