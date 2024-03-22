from setuptools import setup, find_packages

setup(
    name='CustomMachineLearningLibrary',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib",
        "pandas",
        "scikit-learn",
        "ipynb"
    ],
    # Add other metadata as needed
)