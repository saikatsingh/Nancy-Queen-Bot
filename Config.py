import os

# True = take from environment (Render/Koyeb)
# False = use local values
ENVIRONMENT = os.environ.get('ENVIRONMENT', True)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("❌ Your API_ID is not a valid integer.")
    
    API_HASH = os.environ.get('API_HASH')
    BOT_TOKEN = os.environ.get('BOT_TOKEN')
    DATABASE_URL = os.environ.get('DATABASE_URL')
    MUST_JOIN = os.environ.get('MUST_JOIN')

    # Safety checks
    if not DATABASE_URL:
        raise Exception("❌ DATABASE_URL is not set! Please add it in Render environment variables.")
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")

    if MUST_JOIN and MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")

else:
    # 🧪 Local test mode: manually fill values here
    API_ID = 29563132
    API_HASH = "b39be032fc0c567d0cda60dbea99606e"
    BOT_TOKEN = "your_bot_token_here"
    DATABASE_URL = "mongodb+srv://leazygirl17:sampa9735@cluster0.wpwwz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    MUST_JOIN = "-1002147914741"

    if DATABASE_URL.startswith("mongodb+srv://"):
        DATABASE_URL = DATABASE_URL.replace("mongodb+srv://", "mongodb+srv://")

    if MUST_JOIN and MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
