from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess
import sys

class PostInstallCommand(install):
    def run(self):
        install.run(self)
        try:
            subprocess.run([sys.executable, '-m', 'mask_key.main'], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running mask_key.main: {e}")

setup(
    name='mask_key',
    version='0.3.1',
    author='krishna agarwal',
    author_email='krishnacool781@gmail.com',
    description='A Python package to generate mask keys.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/krishnaagarwal781/mask_keys_server',
    packages=find_packages(),
    install_requires=[
        'requests',
        'python-dotenv',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    cmdclass={
        'install': PostInstallCommand,
    }
)
