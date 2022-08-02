from distutils.core import setup
setup(
  name = 'begetAPI',
  packages = ['begetAPI'],
  version = '0.0.2',
  license='GNU General Public License v3.0',
  description = 'Wrapper for Beget API',
  long_description = """
  Python wrapper for https://beget.com/en/kb/api
  """,
  author = 'Alex Kiselev',
  author_email = 'cry0this@gmail.com',
  url = 'https://github.com/cry0this/begetAPI',
  download_url = 'https://github.com/cry0this/begetAPI/archive/refs/tags/v0.0.2.tar.gz',
  keywords = ['api', 'beget'],
  install_requires=[
    'requests',
    'aiohttp'
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)
