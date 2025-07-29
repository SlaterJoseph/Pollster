from dotenv import dotenv_values

config = dotenv_values(".env")
db_name, db_password, db_url = None, None, None

def adjust_method(env: str) -> None:
    """
    Loads the type of variables needed (dev, test, prod)
    :param env: Variant needed
    :return:
    """
    global db_name, db_password, db_url
    env = env.upper()  # make it DEV, TEST, PROD
    db_name = config.get(f"{env}_DB_NAME")
    db_password = config.get(f"{env}_DB_PASSWORD")
    db_url = config.get(f"{env}_DB_URL")

    if not all([db_name, db_password, db_url]):
        raise ValueError(f"Incomplete config for environment: {env}")
