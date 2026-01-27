# conftest.py

import pytest

@pytest.fixture(scope="function")
def sample_numbers():
    print("\nCreating sample numbers")
    return (10, 5)

@pytest.fixture(scope="module")
def module_resource():
    print("\nSetup module resource")
    yield "RESOURCE"
    print("\nTeardown module resource")
