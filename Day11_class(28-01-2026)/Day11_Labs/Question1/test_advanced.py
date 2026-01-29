def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="Environment to run tests against (dev / prod)"
    )


import pytest

@pytest.fixture
def env(request):
    return request.config.getoption("--env")


def test_environment_based(env):
    if env == "prod":
        assert True
    else:
        assert True