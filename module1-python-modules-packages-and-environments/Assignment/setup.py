"""
lamb_martin - Some Data Science helper functions.
"""

import setuptools

REQUIRED = [
    "numpy",
    "pandas"
]

#with open("README.md", "r") as fh:
#    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name="lamb_martin",
    version="0.0.4",
    author="martin-lehman",
    description="Some Data Science helper functions.",
    #long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/martinclehman/doesntexist",
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_required=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)