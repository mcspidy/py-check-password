import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("M@nLen8", False),
        ("Qwerty123$", True),
        ("Qwerty123", False),
        ("qwerty123$", False),
        ("QWERTY123$", True),
        ("Qwerty$", False),
        ("Qwerty1234$", True),
        ("Qwerty12345", False),
        ("Qwerty1234", False),
        ("Qwerty$123", True),
        ("Qwerty$1234", True),
        ("Qwerty$12345", True),
        ("Qwerty17M@xLength", False),
        ("Qwerty1M@xLength", True),
        ("Qwerty$TooLong1", True),
    ]
)
def test_check_password(password: str, expected: str) -> None:
    assert check_password(password) == expected
