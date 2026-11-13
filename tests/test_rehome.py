import os
from importlib.machinery import SourceFileLoader
from importlib.util import module_from_spec, spec_from_loader

SCRIPT = os.path.join(os.path.dirname(__file__), '..', 'rehome')
loader = SourceFileLoader('rehome', SCRIPT)
Rehome = module_from_spec(spec_from_loader('rehome', loader))
loader.exec_module(Rehome)


def test_normalize_repo():
    assert '.' == Rehome.normalize_repo('.')
    assert 'git@github.com:a/b' == Rehome.normalize_repo('a/b')
