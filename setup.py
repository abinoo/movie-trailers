from distutils.core import setup

setup(
    name='My Tomatoes',
    version='0.1.0',
    author='Abin Oommen',
    author_email='abin.oommen@outlook.com',
    packages=['my tomatoes', 'fresh_tomatoes'],
    scripts=['my tomatoes.py','fresh_tomatoes.py'],
    url='https://github.com/abinoo/movie-trailers',
    description='Open youtube videos with a click of a picture',
    long_description=open('README.txt').read(),
    install_requires=[],
)
