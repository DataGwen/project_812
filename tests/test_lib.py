from package.lib import whats_my_name


def test_whoami():

    res = whats_my_name()

    assert "Gwénaël" in res.split()