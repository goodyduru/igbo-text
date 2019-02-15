import setuptools

with open("README.md", "r", encoding='utf-8') as readme:
    long_description = readme.read()

setuptools.setup(
    name="igbo-text-goodyduru",
    version="0.1.0",
    author="Goodness Duru",
    author_email="goodyduru@gmail.com",
    description="A python package for tokenizing and normalizing texts mainly written in the Igbo Language",
    long_description_content_type="text/markdown",
    url="https://github.com/goodyduru/igbo-text",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)