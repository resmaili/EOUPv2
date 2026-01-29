from setuptools import setup, find_packages

setup(
    name="eoupv2",
    version="1.0.0",
    description="Earth Observations Using Python - Second Edition",
    author="Rebekah Esmaili",
    author_email="eoup.book@gmail.com",
    url="https://github.com/resmaili/EOUPv2",
    
    packages=find_packages(),
    
    install_requires=[
        "cartopy>=0.20",
        "matplotlib>=3.5",
        "numpy>=1.20",
        "pandas>=1.3",
        "Py6S>=1.9",
        "pvlib>=0.9",
        "satpy>=0.30",
        "scipy>=1.7",
        "scikit-learn>=1.0",
        "torch>=1.9",
        "torchvision>=0.10",
        "xarray>=0.21",
    ],
    
    package_data={
        "eoupv2": ["datasets/manifest.json"],
    },
    
    python_requires=">=3.9",
    
    license="MIT",

    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
    ],
)