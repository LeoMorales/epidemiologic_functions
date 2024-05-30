from setuptools import find_packages, setup
from os import path

working_directory = path.abspath(path.dirname(__file__))

with open(path.join(working_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="epidemiologic_funtions",
    version="0.0.1",
    description="A simple Python package for epidemiologic studies",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LeoMorales/isonymic-package",
    author="LeoMorales",
    author_email="moralesleonardo.rw@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
    ],
    install_requires=["pandas"],
    python_requires=">=3.6",
)

# python setup.py sdist bdist_wheel
# twine upload --repository-url <repository-url> dist/*
# twine upload --repository-url https://github.com/LeoMorales/epidemiologic_functions dist/*

