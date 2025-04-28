from setuptools import setup, find_packages

setup(
    name="dataforge",
    version="0.1.0",
    author="Moustafa Mohamed",
    description="A data analysis helper library using pandas and tabulate",
    package_data=[
        "pandas",
        "tabulate"
    ],
    python_requires=">=3.7"
)