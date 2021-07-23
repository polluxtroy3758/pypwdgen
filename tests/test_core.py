from pypwdgen.core import Password
import pytest


def test_password(length: int = 9, complexity: int = 3):
    password = Password(length, complexity)
    assert password.length == length
    assert password.complexity >= complexity
    assert password.password == str(password)
    assert f"Password: {password.password}\tComplexity: {password.complexity}" == password.__repr__()


@pytest.mark.parametrize(('length', 'complexity', 'message'), (
    (8, 3, "Given length: 8"),
    (51, 3, "Given length: 51"),
    (9, 2, "Given complexity: 2"),
    (9, 5, "Given complexity: 5"),
))
def test_password_validate_parameters(length: int, complexity: int, message: str):
    with pytest.raises(ValueError) as e:
        Password(length, complexity)
    assert message in str(e.value)
