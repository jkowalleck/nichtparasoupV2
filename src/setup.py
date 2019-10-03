import setuptools

setuptools.setup(
    name="nichtparasoup",
    setup_requires=["setuptools-scm", "setuptools>=40.0"],
    packages=['nichtparasoup', 'nichtparasoup.crawler'],
    package_dir={
        '': 'src'
    },
    python_requires='>=3.4',
)
