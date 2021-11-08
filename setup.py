import os
import re

import setuptools

with open("README.md") as fh:
    long_description = fh.read()

def get_version(*file_paths):
    """
    Extract the version string from the file at the given relative path fragments.
    """
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                            version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')

VERSION = get_version('zappa_manage', '__init__.py')


setuptools.setup(
    name="zappa-manage",
    version=VERSION,
    author="edX-DevOps",
    author_email="devops@edx.org",
    description="Official Manage Package for edX Zappa Bots",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/edx/zappa-manage",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    zip_safe=True,
    python_requires=">=3.8",
    entry_points='''
        [console_scripts]
        zappa_manage=scripts.zappa_manage:cli
    ''',
)
