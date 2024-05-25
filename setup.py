from setuptools import setup, find_packages

setup(
    name='keyguardian',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'keyguardian-setup=keyguardian.cli:setup',
        ],
    },
    install_requires=[
        'requests',
        'python-dotenv'
    ],
)