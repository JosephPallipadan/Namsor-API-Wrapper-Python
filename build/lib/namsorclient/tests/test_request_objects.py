import namsorclient
import pytest


def test():
    with pytest.raises(Exception):
        assert namsorclient.NamsorClient('1132')
