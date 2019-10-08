import setuptools

setuptools.setup(
    name="nichtparasoup",
    version="0.0.1",  # @TODO set versions
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.5",
    install_requires=[
    ],
    extras_require={
        "develop": [
            "tox"  # realy needed ?
        ],
        "testing": [
            "flake8",
            # 'flake8-annotations;python_version>="3.6"',
            # 'flake8-bugbear;python_version="3.5"',
            # flake8-isort;python_version>="3.5"  # enable when we have a auto-fixer in place
            # 'flake8-pep3101;python_version>="3.5"',
            "pep8-naming",
            "mypy -v",
            "pytest",
            "coverage",
            "ddt"
        ]
    }
)
