from setuptools import setup, find_packages

setup(
    name="uncertainarity",
    version="0.1",
    description="testing some ideas with predictive uncertainty",
    author="josh attenberg",
    author_email="jattenbe@stern.nyu.edu",
    url="https://github.com/jattenberg/uncertainarity",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "scipy",
        "numpy",
        "jupyter",
        "matplotlib",
        "seaborn",
        "sklearn",
        "uncertainty-toolbox @ git+https://github.com/uncertainty-toolbox/uncertainty-toolbox.git#master",
    ],
)
