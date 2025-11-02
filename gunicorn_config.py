"""Configuration Gunicorn pour l'environnement de production."""
import multiprocessing
import os

# Nombre de workers - utilise une formule standard mais limite le maximum
workers = min(multiprocessing.cpu_count() * 2 + 1, 3)  # Limite à 3 workers max pour Render
threads = 2  # Nombre de threads par worker

# Timeouts
timeout = 120  # 2 minutes
graceful_timeout = 30

# Limites de mémoire et autres paramètres de performance
max_requests = 1000
max_requests_jitter = 50
worker_class = 'gthread'  # Utilise des threads plutôt que des processus
worker_tmp_dir = '/dev/shm'  # Utilise la mémoire RAM pour les fichiers temporaires

# Logs
accesslog = '-'  # stdout
errorlog = '-'   # stderr
loglevel = os.getenv('GUNICORN_LOG_LEVEL', 'info')

# Paramètres de limitation de ressources
limit_request_line = 4094
limit_request_fields = 100
limit_request_field_size = 8190