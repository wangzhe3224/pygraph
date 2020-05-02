import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pygraph",
    version="0.0.1",
    author="Zhe",
    author_email="wangzhetju@gmail.com",
    description="A library to interact with graphs in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wangzhe3224/pygraph",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)