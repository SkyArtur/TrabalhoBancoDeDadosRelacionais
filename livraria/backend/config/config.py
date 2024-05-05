import os
from dotenv import load_dotenv
from pathlib import Path
from .connector import Connector

load_dotenv()

ROOT_DIR = Path(__file__).parent.parent.absolute()


class Config(Connector):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.root_dir = ROOT_DIR
        self.sql_dir = self.root_dir.joinpath('mysql')


session = Config(params={
    'database': os.getenv('DATABASE'),
    'user': os.getenv('USER'),
    'password': os.getenv('PASSWORD'),
    'host': os.getenv('HOST'),
    'port': os.getenv('PORT'),
})
