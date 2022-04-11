from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='calculator',
    version='0.0.9',
    description='Functional calculator',
    py_modules=["calculator"],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=3.7",
        ],
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VilkaMini/calculatorApp",
    author="Vilius Alaunis",
    author_email="viliusalaunis@gmail.com",
)