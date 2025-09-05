from setuptools import setup, find_packages

setup(
    name="busybee-backend",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "Flask==3.1.2",
        "Flask-CORS==6.0.1",
    ],
)
