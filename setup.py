import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mfish",
    version="1.0",
    author="Polina",
    packages=["mfish"],
    python_requires='>=3.6',
)
