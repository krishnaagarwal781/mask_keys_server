from setuptools import setup, find_packages
from setuptools.command.install import install
import importlib.util

class PostInstallCommand(install):
    def run(self):
        install.run(self)  # Ensures that the install proceeds as normal
        print("Post-installation command executed successfully.")
        try:
            print("Attempting to execute main() function...")
            spec = importlib.util.spec_from_file_location(
                "mask_key.main", "mask_key/main.py"
            )
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            module.main()
            print("main() function executed successfully.")
        except Exception as e:
            print(f"Error running main(): {e}")

setup(
    name="mask_key",
    version="0.3.2",
    author="krishna agarwal",
    author_email="krishnacool781@gmail.com",
    description="A Python package to generate mask keys.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/krishnaagarwal781/mask_keys_server",
    packages=find_packages(),
    install_requires=[
        "requests",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "mask-key-setup=mask_key.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    cmdclass={
        "install": PostInstallCommand,
    },
)
