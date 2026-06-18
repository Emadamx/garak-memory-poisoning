from setuptools import setup, find_packages

setup(
    name="garak-memory-poisoning",
    version="0.1.0",
    author="Muhammad Adam",
    author_email="madam2@andrew.cmu.edu",
    description="Memory poisoning test probes for the Garak LLM vulnerability scanner",
    url="https://github.com/Emadamx/garak-memory-poisoning",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=["garak>=0.9.0"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
