<<<<<<< HEAD
#!C:\Users\marci\CURSO_PHYTON_APLICATIVO\venv\Scripts\python.exe
=======
#!C:\Users\marci\CURSO_PHYTON_APLICATIVO\venv\Scripts\python.exe
>>>>>>> 1651482b46c304b36ab1d5056382003c08636891
# When the django-admin.py deprecation ends, remove this script.
import warnings

from django.core import management

try:
    from django.utils.deprecation import RemovedInDjango40Warning
except ImportError:
    raise ImportError(
        'django-admin.py was deprecated in Django 3.1 and removed in Django '
        '4.0. Please manually remove this script from your virtual environment '
        'and use django-admin instead.'
    )

if __name__ == "__main__":
    warnings.warn(
        'django-admin.py is deprecated in favor of django-admin.',
        RemovedInDjango40Warning,
    )
    management.execute_from_command_line()
