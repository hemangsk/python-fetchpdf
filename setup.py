from setuptools import setup, find_packages
setup(
    name="FetchPDF",
    version="0.1",
    packages=["fetchpdf"],
    scripts=['fetchpdf.py'],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=['docutils>=0.3'],

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst']

    },
    entry_points = {
        "console_scripts": ['fetchpdf = fetchpdf.fetchpdf:main']
    },

    # metadata for upload to PyPI
    author="Hemang Kumar",
    author_email="hemangsk@gmail.com",
    description="Fetches all .pdf files from a link, faster than ligh...sound",
    license="GPLv3",
    keywords="fetch pdf link scrape fetchpdf",
    url="http://github.com/hemangsk/python-fetchpdf",   # project home page, if any

    # could also include long_description, download_url, classifiers, etc.
)
