from distutils.core import setup

setup(name="coussin",
      version="0.0.1",
      description="Async couchdb 2.0 client",
      author="Florent D'halluin",
      author_email="flal@melix.net",
      packages=("coussin",),
      requires=("aiohttp >= 3.2")
)

      
