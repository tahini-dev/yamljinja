import pytest

import yamljinja.core


@pytest.mark.parametrize('args, kwargs', [
    ([], dict()),
])
def test_NullUndefined_init(args, kwargs):
    assert isinstance(yamljinja.core.NullUndefined(*args, **kwargs), yamljinja.core.NullUndefined)


@pytest.mark.parametrize('null_undefined, key, expected', [
    # (yamljinja.core.NullUndefined(), None, ''),
    (yamljinja.core.NullUndefined(), 'test_key', ''),
])
def test_NullUndefined_getattr(null_undefined, key, expected):
    assert getattr(null_undefined, key) == expected


@pytest.mark.parametrize('args, kwargs, expected', [
    (
        [
            '''var1: val1
var2: val2
var3: '{{var1}}-{{var2}}'
''',
        ],
        {},
        {
            'var1': 'val1',
            'var2': 'val2',
            'var3': 'val1-val2',
        },
    )
])
def test_load(args, kwargs, expected):
    actual = yamljinja.core.load(*args, **kwargs)
    assert actual == expected
