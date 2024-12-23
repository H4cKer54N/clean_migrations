from setuptools import setup, find_packages

setup(
    name="clean_migrations",
    version="1.0.0",
    description="Herramienta para limpiar migraciones en proyectos Django",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="H4cker54n",
    author_email="snbq89@gmail.com",
    url="https://github.com/h4cker54n/clean_migrations",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "clean-migrations=clean_migrations.main:clean_migrations",
        ],
    },
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Django",
    ],
    install_requires=[],
)
