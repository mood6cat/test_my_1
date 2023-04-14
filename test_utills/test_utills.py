from utills.dicts import get_val
import pytest

@pytest.fixture
def data():
    return [{"vcs": "mercurial"}, {}]

def test_get_val(data):
    data1, data2 = data
    assert get_val(data1, "vcs") == "mercurial"
    assert get_val(data1, '') == "git"
    assert get_val(data2, '')=="git"
    assert get_val(data2, '', "bazaar") == "bazaar"



