"""Test to ensure package loads correctly."""

try:
    import mason_server
except ImportError:
    mason_server = None


def test_package_loads():
    assert mason_server is not None
