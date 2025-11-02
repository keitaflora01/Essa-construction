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

# Ensure project root and the inner `essa_construction` package are on sys.path.
# Some deploy environments run from a different working directory; adding the
# project root makes `import config.settings` (and similar) reliable.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
# Prefer project root first so `config` package is importable.
project_root = str(BASE_DIR)
essa_pkg = str(BASE_DIR / "essa_construction")
if project_root not in sys.path:
	sys.path.insert(0, project_root)
if essa_pkg not in sys.path:
	sys.path.insert(0, essa_pkg)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

# Get WSGI application callable for servers/gateways to use
application = get_wsgi_application()
