import pytest

def admin_command(command, sudo=True):
    if sudo:
        command = ["sudo"] + command
    return command


class TestAdminCommand:
    def command(self):
        return ["ps", "aux"]

    def test_no_sudo(self):
        result = admin_command(self.command(), sudo=False)
        assert result == self.command()

    def test_sudo(self):
        result = admin_command(self.command(), sudo=True)
        expected = ["sudo"] + self.command()
        assert result == expected

if __name__ == '__main__':
    pytest.main()