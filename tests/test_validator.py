from main import PasswordValidator


def test_password():
    validator = PasswordValidator()
    assert validator.validate_password("abcdefggasdfsa") == False
    assert validator.validate_password("abcdefg123") == False
    assert validator.validate_password("abc") == False
    assert validator.validate_password("Abcdefg123456") == True
