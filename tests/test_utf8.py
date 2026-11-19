import pytest

from codec import utf8 as mod

CASES = [
    ('encode_codepoint', [65], [65], False),
    ('encode_codepoint', [20013], [228, 184, 173], False),
    ('decode_bytes', [[65]], [65, 1], False),
    ('decode_bytes', [[228, 184, 173]], [20013, 3], False),
    ('validate', [[228, 184, 173]], True, False),
    ('validate', [[228, 40]], False, False),
    ('encode_str', ['A中'], [65, 228, 184, 173], False),
    ('decode_str', [[65, 228, 184, 173]], 'A中', False),
    ('encode_codepoint', [0], [0], False),
    ('decode_bytes', [[195, 169]], [233, 2], False),
    ('validate', [[65]], True, False),
    ('validate', [[]], True, False),
    ('encode_str', [''], [], False),
    ('decode_str', [[]], '', False),
    ('encode_str', ['é'], [195, 169], False),
]


@pytest.mark.parametrize("func_name,args,expected,approx", CASES)
def test_utf8_contract(func_name, args, expected, approx):
    func = getattr(mod, func_name)
    result = func(*args)
    if approx:
        assert result == pytest.approx(expected)
    else:
        assert result == expected
