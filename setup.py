from setuptools import setup
setup(
    name = 'YoutubeMiniTool',
    version = '0.1.0',
    packages = ['audioModule','core'],
    entry_points = {
        'console_scripts': [
            'core = core.__main__:main'
        ]
    })