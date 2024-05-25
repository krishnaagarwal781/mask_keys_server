from setuptools import setup, find_packages

setup(
    name='mask_key',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'mask-key-setup=mask_key.cli:setup',
        ],
    },
    install_requires=[
        'requests',
        'python-dotenv'
    ],
)