import os

from setuptools import setup

if __name__ == "__main__":
    os.environ["SETUPTOOLS_SCM_PRETEND_VERSION_FOR_PY-CORD"] = "2.5.6"
    setup()
