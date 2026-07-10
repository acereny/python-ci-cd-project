from app import calculate_telecom_tax


def test_calculate_telecom_tax():
    result = calculate_telecom_tax(100, 10)
    assert result == 110