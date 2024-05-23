from setuptools import setup, find_packages

setup(
    name='mask_key',  # The name of your package
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A Python package to generate mask keys.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/mask_key',
    packages=find_packages(),
    install_requires=[
        'requests',
        'python-dotenv',
    ],
    entry_points={
        'console_scripts': [
            'mask-key=mask_key.main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
