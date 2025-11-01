"""Compatibility shim for WSGI entrypoint.

Some deployment platforms (or old configs) expect the WSGI app at
`essa_construction.wsgi:application`. This project keeps the real
WSGI in `config/wsgi.py`. Import and re-export the application here
so both import paths work.
"""
from __future__ import annotations

from config.wsgi import application  # re-export the Django WSGI application

__all__ = ["application"]
