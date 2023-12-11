from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("afaas-custom-package")
except PackageNotFoundError:
    __version__ = "unknown version"
