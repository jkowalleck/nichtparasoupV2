import setuptools

setuptools.setup(
    name="nichtparasoup",
    version="dev",  # TODO add versions
    packages=setuptools.find_packages(where='src'),
    package_dir={'': 'src'},
    python_requires='>=3.4',
    install_requires=[
        "typing",
    ],
    extras_require={
        "develop": [
        ],
        "testing": [
            "ddt",
            "pytest",
            "pytest-cov",
            "codecov",
        ],
    },
)
