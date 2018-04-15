import os

# This file is exec'd from settings.py, so it has access to and can
# modify all the variables in settings.py.

DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "*m7k#bnu8##_n!h&=29eaqtmj3nf-9udj%53x(u@6bs6n8$p&9"
NEVERCACHE_KEY = "a7u#b+mi3sej^pxl^*&k05w0e_=us4+so1s=pv^ayr%!7=)5+p"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.postgresql",
        # DB name or path to database file if using sqlite3.
        "NAME": os.environ['DATABASE_NAME'],
        # Not used with sqlite3.
        "USER": os.environ['DATABASE_USER'],
        # Not used with sqlite3.
        "PASSWORD": os.environ['DATABASE_PASSWORD'],
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": os.environ['DATABASE_HOST'],
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "5432",
    }
}

###################
# DEPLOY SETTINGS #
###################

# Domains for public site
ALLOWED_HOSTS = ["randyforcongress.herokuapp.com"]

# These settings are used by the default fabfile.py provided.
# Check fabfile.py for defaults.

# FABRIC = {
#     "DEPLOY_TOOL": "rsync",  # Deploy with "git", "hg", or "rsync"
#     "SSH_USER": "",  # VPS SSH username
#     "HOSTS": [""],  # The IP address of your VPS
#     "DOMAINS": ALLOWED_HOSTS,  # Edit domains in ALLOWED_HOSTS
#     "REQUIREMENTS_PATH": "requirements.txt",  # Project's pip requirements
#     "LOCALE": "en_US.UTF-8",  # Should end with ".UTF-8"
#     "DB_PASS": "",  # Live database password
#     "ADMIN_PASS": "",  # Live admin user password
#     "SECRET_KEY": SECRET_KEY,
#     "NEVERCACHE_KEY": NEVERCACHE_KEY,
# }
