from setuptools import setup, find_packages


setup(
    name='ruledump',
    version='0.1',
    license='MIT',
    author="François Amat",
    author_email='contact@famat.me',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/famat-thesis/ruledump',
    keywords='sql rule-mining knowledge',
    install_requires=[
      ],

)
