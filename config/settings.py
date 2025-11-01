"""Compatibility shim: expose project's settings as `config.settings`.

Some deployment platforms (or environment variables) may point
DJANGO_SETTINGS_MODULE at `config.settings`. The real settings live in
`essa_construction.settings`. Import everything here so both import
paths work.
"""
from __future__ import annotations

# Re-export settings from the package's settings module
from essa_construction.settings import *  # noqa: F401,F403
