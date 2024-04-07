#!/usr/bin/env python
"""Run administrative tasks."""
import os
from django.core.management import execute_from_command_line

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Online_Auction.settings')
    try:
        execute_from_command_line(['manage.py', 'runserver', '0.0.0.0:8080'])
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc


if __name__ == '__main__':
    main()
