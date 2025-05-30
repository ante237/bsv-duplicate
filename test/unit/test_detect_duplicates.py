import pytest
from unittest.mock import patch
from src.util.detector import detect_duplicates
# develop your test cases here



@pytest.mark.unit
@patch("src.util.detector.parse", return_value=[])
def test_detect_duplicates_1(mock_parse):
    
    ret = detect_duplicates("")

    assert ret == []

@pytest.mark.unit
def test_detect_duplicates_2():
    assert True

@pytest.mark.unit
def test_detect_duplicates_3():
    assert True

@pytest.mark.unit
def test_detect_duplicates_4():
    assert True

@pytest.mark.unit
def test_detect_duplicates_5():
    assert True

@pytest.mark.unit
def test_detect_duplicates_6():
    assert True