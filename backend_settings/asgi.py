"""
ASGI config for backend_settings project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter #для чата
from channels.auth import AuthMiddlewareStack #для чата
import app_foodrecipes.routing #для чата

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_settings.settings')

# application = get_asgi_application() было до чата

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            app_foodrecipes.routing.websocket_urlpatterns
        )
    )
})
