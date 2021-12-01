"""
Release and publish GDBIGtools to PyPI.

Author: Chengrui Wang
Date: 2021-11-30
"""
from importlib import util
from subprocess import call

spec = util.spec_from_file_location("_", "./setup.py")
module = util.module_from_spec(spec)
spec.loader.exec_module(module)

#call(["pandoc", "--from=markdown", "--to=rst", "-o", "README.rst", "README.md"])
call(["python", "setup.py", "sdist"])
tarball = "dist/{}-{}.tar.gz".format(module.meta.__DISTNAME__, module.meta.__VERSION__)
call(["twine", "upload", "-r", "pypi", tarball])

