import subprocess

import pytest
import testinfra


# scope='session' uses the same container for all the tests;
# scope='function' uses a new container per test function.
@pytest.fixture(scope='session')
def host(request):
    image = request.config.getoption("--image")
    tag = request.config.getoption("--tag")
    # run a container
    docker_id = subprocess.check_output(
        ['docker', 'run', '-d', '--privileged', '-v/sys/fs/cgroup:/sys/fs/cgroup:ro', f'nbjwl/molecule:{image}.{tag}']).decode().strip()
    # return a testinfra connection to the container
    yield testinfra.get_host("docker://" + docker_id)
    # at the end of the test suite, destroy the container
    subprocess.check_call(['docker', 'rm', '-f', docker_id])


@pytest.mark.parametrize("command", [
    "systemctl status"
])
def test_service_config(host, command):
    cmd = host.run(command)
    assert cmd.succeeded
