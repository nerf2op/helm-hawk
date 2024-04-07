import pytest
from click.testing import CliRunner
from cli.main import cli

# Tests for diff command
def test_diff_command():
    runner = CliRunner()
    result = runner.invoke(cli ,args=['diff'])
    assert result.exit_code == 0
    assert 'Group of commands for comparing two versions of helm chart' in result.output

# Tests for get command
def test_get_command():
    runner = CliRunner()
    result = runner.invoke(cli,args=['get'])
    assert result.exit_code == 0
    assert 'Group of commands  to retrieve information from the server' in result.output

# # Tests for history command
def test_history_command():
    runner = CliRunner()
    result = runner.invoke(cli,args=['history'])
    assert result.exit_code == 2  # As it requires RELEASE_NAME
    assert "Error: Missing argument 'RELEASE_NAME'." in result.output

# Tests for list command
def test_list_command():
    runner = CliRunner()
    result = runner.invoke(cli,args=['list','--help'])
    assert result.exit_code == 0
    assert 'This command lists all of the releases' in result.output

# # Tests for pull command
def test_pull_command():
    runner = CliRunner()
    result = runner.invoke(cli, ['pull','--help'])
    assert result.exit_code == 0
    assert 'Retrieve a package from a package repository' in result.output

# # Tests for repo command
def test_repo_command():
    runner = CliRunner()
    result = runner.invoke(cli,['repo','--help'])
    assert result.exit_code == 0  # As it requires COMMAND
    assert 'This command consists of multiple subcommands' in result.output

# Tests for rollback command
def test_rollback_command():
    runner = CliRunner()
    result = runner.invoke(cli, ['rollback', '--help'])
    assert result.exit_code == 0
    assert 'This command rolls back a release to a previous revision' in result.output

# Tests for status command
def test_status_command():
    runner = CliRunner()
    result = runner.invoke(cli, ['status','--help'])
    assert result.exit_code == 0
    assert 'This command shows the status of a named release' in result.output

# Tests for template command
def test_template_command():
    runner = CliRunner()
    result = runner.invoke(cli, ['template', '--help'])
    assert result.exit_code == 0
    assert 'Render chart templates locally and display the output' in result.output

# # Tests for uninstall command
def test_uninstall_command():
    runner = CliRunner()
    result = runner.invoke(cli, ['uninstall','--help'])
    assert result.exit_code == 0
    assert 'This command takes a release name and uninstalls the release' in result.output

# Tests for upgrade command
def test_upgrade_command():
    runner = CliRunner()
    result = runner.invoke(cli, ['upgrade', '--help'])
    assert result.exit_code == 0
    assert 'This command upgrades a release to a new version of a chart' in result.output

if __name__ == "__main__":
    pytest.main()
