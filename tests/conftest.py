import pytest

def pytest_addoption(parser):
  parser.addoption("--api_key", action="store")
  parser.addoption("--engine", action="store")


@pytest.fixture(scope="session")
def api_key(request):
  api_key = request.config.option.api_key

  if api_key is None:
    pytest.skip()

  return api_key

@pytest.fixture(scope="session")
def engine(request):
  engine = request.config.option.engine

  if engine is None:
    pytest.skip()

  return engine