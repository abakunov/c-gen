from setuptools import setup, find_packages

setup(
    name="code_generator",
    version="1.0",
    packages=find_packages(),
    py_modules=["effect_generators", "code_generators", "dataset_generator", "main"],
    entry_points={
        "console_scripts": [
            "c-gen=main:main",
        ],
    },
    install_requires=[
        "pillow",
        "treepoem",
        "numpy",
    ],
)
