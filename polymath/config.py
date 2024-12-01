import os
import shutil
from polymath import utils
import toml


class Config:
    def extract(self, file_name, template_name):
        config_file = utils.get_path(file_name)
        print(f"Attempting to access config file at: {config_file}")
        if not os.path.isfile(config_file):
            self.configured = False
            print(f"config {config_file} doesn't exist, copying template!")
            shutil.copyfile(utils.get_path(template_name), config_file)
        else:
            self.configured = True
        return config_file


class TomlConfig(Config):
    def __init__(self, file_name, template_name):
        self.configured = True
        config_file = self.extract(file_name, template_name)
        self.load(config_file)

    def load(self, config_file):
        self._config = toml.load(config_file)

    def __getitem__(self, key):
        return self._config[key]