from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup (
    name="images-processing-elisio",
    version="0.0.1",
    author="Elisio Moura",
    author_email="elisiomou@gmail.com",
    description="Image Processing Package using Skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ElisioMou/Images-Processing-Package.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)