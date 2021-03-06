import pytest
from click.testing import CliRunner, Result

from .. import cli


@pytest.fixture
def invoke_cli():
    def invoke(*args: str) -> Result:
        runner = CliRunner()
        return runner.invoke(cli, args)

    return invoke
