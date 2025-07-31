from dotenv import dotenv_values

class EnvConfig:
    def __init__(self):
        self.db_name = None
        self.db_user = None
        self.db_password = None
        self.db_url = None
        self.security_key = None
        self.config = dotenv_values(".env")

    def adjust_env(self, env: str):
        env = env.upper()
        self.db_name = self.config.get(f"{env}_DB_NAME")
        self.db_user = self.config.get(f"{env}_DB_USER")
        self.db_password = self.config.get(f"{env}_DB_PASSWORD")
        self.db_url = self.config.get(f"{env}_DB_URL")
        self.security_key = self.config.get("SECURITY_KEY")

        if not all([self.db_name, self.db_user, self.db_password, self.db_url, self.security_key]):
            raise ValueError(f"Incomplete config for environment: {env}")

env_config = EnvConfig()