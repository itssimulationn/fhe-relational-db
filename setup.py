from setuptools import setup, find_packages

setup(
    name="fhe-relational-db",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "concrete-ml",
        "numpy",
        "pandas",
        "sqlparse",
        "fastapi",
        "uvicorn",
        "pydantic",
    ],
)
