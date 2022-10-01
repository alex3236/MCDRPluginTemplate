import subprocess
import sys
import importlib
import pkg_resources
import ruamel.yaml as yaml

install = True

try:
    mcdr = pkg_resources.get_distribution("mcdreforged")
    if mcdr.parsed_version > pkg_resources.parse_version('2.2.0'):
        print(f'MCDReforged ({mcdr.version}) installed. Skipping install process.')
        install = False
except pkg_resources.DistributionNotFound:
    pass

if install:
    print('Installing MCDReforged...')
    subprocess.check_call([sys.executable, "-m", "pip", "install", "mcdreforged"])

print('Initializing MCDReforged...')
subprocess.check_call([sys.executable, "-m", "mcdreforged", "init"])

print('Preparing plugin developing environment...')
yaml = importlib.import_module('ruamel.yaml')
yamler = yaml.YAML()
yamler.explicit_start = True
with open('config.yml', 'r', encoding='utf8') as f:
    config = yamler.load(f)

config['plugin_directories'][0] = '.'
config['language'] = 'zh_cn'
config['debug']['plugin'] = True

with open('config.yml', 'w', encoding='utf8') as f:
    yamler.dump(config, f)
