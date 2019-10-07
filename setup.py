import setuptools


setuptools.setup(
    name="nichtparasoup",
    version="0.0.0",  # @TODO set versions
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.4",
    install_requires=[
        'typing;python_version<="3.4"',
    ],
    extras_require={
        "testing": [
            "pytest",
            "coverage",
            "ddt",
        ]
    }
)
