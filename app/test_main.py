from app.main import check_password


def test_check_password() -> None:
    assert check_password("I@m12") is False, \
        "Password must be at least 8 characters long"
    assert check_password("Qwerty123$") is True, \
        "Password is within parameters"
    assert check_password("Qwerty123") is False, \
        "Password must contain at least one special character"
    assert check_password("qwerty123$") is False, \
        "Password must contain at least one uppercase letter"
    assert check_password("QWERTY123$") is True, \
        "Password is within parameters"
    assert check_password("Qwerty$") is False, \
        "Password must contain at least one digit"
    assert check_password("Qwerty1234$") is True, \
        "Password is within parameters"
    assert check_password("Qwerty12345") is False, \
        "Password must contain at least one special character"
    assert check_password("Qwerty1234") is False, \
        "Password must contain at least one special character"
    assert check_password("Qwerty$123") is True, \
        "Password is within parameters"
    assert check_password("Qwerty$1234") is True, \
        "Password is within parameters"
    assert check_password("Qwerty$12345") is True, \
        "Password is within parameters"
    assert check_password("Qwerty$MaxLength") is False, \
        "Password cannot be longer than 12 characters"
    assert check_password("Qwerty1M@xLength") is True, \
        "Password is within parameters"
    assert check_password("Qwerty$TooLong1") is True, \
        "Password is within parameters"
