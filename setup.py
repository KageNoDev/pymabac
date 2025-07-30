from setuptools import setup, find_packages

setup(
    name="mabac_app",
    version="0.1.0",
    description="A GUI-based MABAC decision support system with sensitivity analysis",
    author="Laura Białobrzewska",
    author_email="lauraura18@wp.pl",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib",
    ],
    python_requires=">=3.7",
    entry_points={
        "gui_scripts": [
            "mabac-gui = main:main",
        ]
    },
)
