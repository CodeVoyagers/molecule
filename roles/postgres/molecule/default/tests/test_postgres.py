
def test_install_postgresql(host):

    postgresql = host.service('postgresql-13')

    assert postgresql.is_running
    assert postgresql.is_enabled
