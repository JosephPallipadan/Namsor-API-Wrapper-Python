# python setup.py sdist bdist_wheel

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="namsor-client",
    version="0.0.3",
    author="Joseph Pallipadan",
    author_email="pallipadanjoseph@gmail.com",
    description="A Wrapper for the Namsor Classification API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
