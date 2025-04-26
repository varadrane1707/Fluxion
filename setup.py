from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="fluxion",
    version="0.1.0",
    author="Varad Rane",
    author_email="varadrane17@gmail.com",
    description="A high-performance inference engine for Flux Models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/varadrane1707/fluxion",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=[
        "torch>=2.0.0",
        "transformers>=4.30.0",
        "numpy>=1.21.0",
        "tqdm>=4.65.0",
        "pillow>=9.0.0",
        "accelerate>=0.20.0",
    ],
    extras_require={
        "dev": [
            "black",
            "isort",
            "flake8",
            "mypy",
            "pytest",
            "pytest-cov",
            "pre-commit",
        ],
    }
) 