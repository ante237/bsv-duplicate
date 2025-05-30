import pytest
from unittest.mock import patch
from src.util.detector import detect_duplicates
# develop your test cases here



@pytest.mark.unit
#Patch parse function to return correct value according to test. This is done for all functions
@patch("src.util.detector.parse", return_value=[])
def test_detect_duplicates_1(mock_parse):
    with pytest.raises(ValueError):
        detect_duplicates("")


@pytest.mark.unit
@patch("src.util.detector.parse", return_value=[{"key": "1", "doi": "testDOI1"}])
def test_detect_duplicates_2(mock_parse):
    with pytest.raises(ValueError):
        detect_duplicates("")

@pytest.mark.unit
@patch("src.util.detector.parse", return_value=[{"key": "1", "doi": "testDOI1"}, {"key": "1", "doi": "testDOI1"}])
def test_detect_duplicates_3(mock_parse):
    ret = detect_duplicates("")
    assert ret == [{"key": "1", "doi": "testDOI1"}]

@pytest.mark.unit
@patch("src.util.detector.parse", return_value=[{"key": "1", "doi": "testDOI1"}, {"key": "2", "doi": "testDOI2"}])
def test_detect_duplicates_4(mock_parse):
    ret = detect_duplicates("")
    assert ret == []

@pytest.mark.unit
@patch("src.util.detector.parse", return_value=[{"key": "1"}, {"key": "1", "doi": "testDOI1"}])
def test_detect_duplicates_5(mock_parse):
    ret = detect_duplicates("")
    assert ret == [{"key": "1", "doi": "testDOI1"}]

@pytest.mark.unit
@patch("src.util.detector.parse", return_value=[{"key": "1"}, {"key": "2", "doi": "testDOI2"}])
def test_detect_duplicates_6(mock_parse):
    ret = detect_duplicates("")
    assert ret == []