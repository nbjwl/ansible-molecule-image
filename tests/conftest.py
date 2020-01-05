def pytest_addoption(parser):
    parser.addoption("--image", action="store", default="debian")
    parser.addoption("--tag", action="store", default="buster")