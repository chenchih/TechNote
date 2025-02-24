import pytest

@pytest.mark.windows
def test_window_1():
    assert True
@pytest.mark.windows
def test_windows():
    assert True
@pytest.mark.nonwindows
def test_ubuntu():
    assert True
@pytest.mark.nonwindows
def test_mac():
    assert True