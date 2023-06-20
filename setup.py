from setuptools import setup
from cx_Freeze import setup, Executable

buildOptions = dict(packages = [], excludes = [])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [Executable('example_1.py', base=base, targetName = 'chat.exe')]
setup(name='chatexampy', #name задает полное имя пакета.
      version = "0.1",
      description = "example chat",
      author = "Liuba Kundas",
      author_email = "kundasl1@gmail.com",
      #url = "http://www.blog.pythonlibrary.org",
      packages=["src"],
      options = dict(build_exe = buildOptions),
      executables = executables,
      #executables = [Executable("src")] #правильно
      )
input("Press Enter")
