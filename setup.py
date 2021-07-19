from setuptools import setup

APP = ['houry.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'icon.icns',
    'plist': {
        'CFBundleShortVersionString': '0.2.0',
        'LSUIElement': True,
    },
}

setup(
    app=APP,
    data_files=['beep.wav'],
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)