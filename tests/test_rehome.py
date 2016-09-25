import Rehome

def test_normalize_repo():
    assert '.' == Rehome.normalize_repo('.')
    assert 'https://github.com/a/b' == Rehome.normalize_repo('a/b')


