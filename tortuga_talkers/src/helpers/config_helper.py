import yaml
from pathlib import Path
from tortuga_talkers.src.models.config import Config

def load_config(filepath: Path) -> Config:
    with open(filepath, "r") as file:
        return Config(**yaml.safe_load(file))