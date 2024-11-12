# setup.py
from setuptools import setup, find_packages

setup(
    name="SimplePythonMusicPlayer",
    version="1.0",
    description="A simple music player app built with Python.",
    author="Ramprasath M K",
    packages=find_packages(),
    install_requires=[
        'pygame>=2.6.1'
        # Include necessary dependencies here, e.g., PyQt5 if using a Qt GUI:
        # 'PyQt5>=5.15.0',
    ],
    entry_points={
        'console_scripts': [
            'musicplayer=src.main:main',  # Adjust 'src.main:main' based on the project's entry point
        ],
    },
)
