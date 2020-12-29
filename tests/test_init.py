import pytest

import yamljinja


@pytest.mark.parametrize('attribute', [
    'load',
])
def test_attribute(attribute):
    assert hasattr(yamljinja, attribute)
