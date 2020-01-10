# from cx_Freeze import setup, Executable

# executables = [Executable('client_final.py', base=None)]

# packages = ['idna']

# options = {
#     'build_exe': {
#         'packages': packages
#     }
# }

# setup(
#     name = 'client',
#     options = options,
#     version = '1',
#     description = 'client script',
#     executables = executables
# )

from distutils.core import setup
import py2exe

setup(console=['client_final.py'])
