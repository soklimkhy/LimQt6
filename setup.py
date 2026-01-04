from setuptools import setup, find_packages

setup(
    name="LimQt6",
    version="0.1.0",
    description="A simple UI component library built on top of PyQt6",
    author="Limkhy Sok",
    author_email="soklimkhy@gmail.com",
    url="https://github.com/soklimkhy/LimQt6",
    packages=find_packages(),
    install_requires=[
        "PyQt6>=6.0.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
