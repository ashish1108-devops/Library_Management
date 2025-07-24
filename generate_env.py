import os

env_type = os.getenv("ENV_TYPE", "local").lower()  # Default is "local"
host = "localhost" if env_type == "local" else "db"

with open(".env.template") as template_file:
    content = template_file.read().replace("{{ DB_HOST }}", host)

with open(".env", "w") as env_file:
    env_file.write(content)

print(f".env generated for {env_type} environment (DB_HOST={host})")
