from os.path import join, dirname, isfile, basename
import glob
import importlib

def get_modules(modules, files, base):
  for file in files:
    if file.endswith('__init__.py'):
      continue
    if isfile(file) and file.endswith('controller.py'):
      path = base + basename(file)[:-3]
      module = importlib.import_module(path)
      setattr(module, 'path', '*')
    else:
      get_modules(modules, glob.glob(join(file, "*")), base + basename(file) + '.')

modules = []
get_modules(modules, glob.glob(join(dirname(__file__), "*")), 'src.app.')