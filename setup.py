import setuptools

setuptools.setup(
    name="nichtparasoup",
    version="dev", # TODO add versions
 #   setup_requires=["setuptools-scm", "setuptools>=40.0"],
    packages=setuptools.find_packages(where='src'),
    package_dir={'': 'src'},
    python_requires='>=3.0',
    install_requires=[
    ],
    extras_require={
        "testing": [
            "ddt",
            "pytest",
            "pytest-cov",
            "codecov",
        ],
    },
)
