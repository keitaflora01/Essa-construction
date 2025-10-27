"""
WSGI config for Essa_construction project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os
import sys
from pathlib import Path

from django.core.wsgi import get_wsgi_application

# This allows easy placement of apps within the interior
# essa_construction directory.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
sys.path.append(str(BASE_DIR / "essa_construction"))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "essa_construction.settings")

# Get WSGI application callable for servers/gateways to use
application = get_wsgi_application()
