import configparser
from dataclasses import dataclass


@dataclass
class WebApp:
    db_host: str
    db_port: str
    db_name : str
    db_user : str
    db_pass : str


@dataclass
class Config:
    web_app: WebApp


def load_config(path: str):
    print(path)
    config = configparser.ConfigParser()
    config.read(path)

    app = config["web_app"]

    return Config(
        web_app=WebApp(
            db_host=app["db_host"],
            db_port=app["db_port"],
            db_name=app["db_name"],
            db_user=app["db_user"],
            db_pass=app["db_pass"],
        )
    )
