import pytest


@pytest.mark.parametrize("test_html, expected", [
    ("><", True),
    (">123<", False),
])
def test_example(test_html, expected):
    # able to read the test case.
    print('aaa' + test_html)
    print(expected)