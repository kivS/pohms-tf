from setuptools import setup

setup(
    name='pohms-tf',
    version='12k20.0.1',
    author='Vik Borges',
    author_email='v1k@protonmail.com',
    py_modules=['pohmstf'],
    install_requires=[
        'Click',
        'Numpy',
        'Tensorflow'
    ],
    entry_points='''
        [console_scripts]
        pohmstf=pohmstf:main_cli
    '''
)