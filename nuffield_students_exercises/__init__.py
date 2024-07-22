from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("nuffield-students-exercises")
except PackageNotFoundError:
    # package is not installed
    pass
