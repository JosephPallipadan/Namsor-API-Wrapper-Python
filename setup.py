import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="namsor-client",
    version="1.0.0",
    author="Joseph Pallipadan",
    author_email="pallipadanjoseph@gmail.com",
    description="A Wrapper for the Namsor Classification API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=['Gender', 'Classify', 'Ethnicity', 'Origin',
              'Country', 'Classifier', 'Namsor', 'Wrapper', 'Name to Gender', 'Name to Ethnicity', 'Name to Origin'],
    url="https://github.com/JosephPallipadan/Namsor-API-Wrapper-Python",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests', 'XlsxWriter'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
