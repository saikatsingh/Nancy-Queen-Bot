import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', True)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    DATABASE_URL = os.environ.get('DATABASE_URL', None)
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', None)
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = 29563132
    API_HASH = "b39be032fc0c567d0cda60dbea99606e"
    BOT_TOKEN = ""
    DATABASE_URL = "mongodb+srv://leazygirl17:sampa9735@cluster0.wpwwz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = "-1002147914741"
    if MUST_JOIN.startswith("@creazy_updates_zone"):
        MUST_JOIN = MUST_JOIN[1:]
