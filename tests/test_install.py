from click.testing import CliRunner
from mycli.cli import cli

def test_install():
    runner = CliRunner()
    result = runner.invoke(cli, ['install'])
    assert result.exit_code == 0
    assert 'Running install scripts...' in result.output
