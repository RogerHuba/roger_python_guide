import pytest

from .multi_bracket_validation import multi_bracket_validation as mbv


class TestMultiBracketValidation:
    
    test_data = (
        
        # Edge Cases
        (')', False),
        ('(', False),
        ('', True),
        ('[}', False),
        
        # Happy Path
        ('{}', True),
        ('{}(){}', True),
        ('()[[Extra Characters]]', True),
        ('(){}[[]]', True),
        ('{}{Code}[Fellows](())', True),
        ('[({}]', False),
        ('(](', False),
        ('{(})', False),
        ('(hello(world[aa{cc{{{}}}ss}]))', True),
        ('(hello(world[aa{cc{{{}}}ss}])()', False),
    )
    @pytest.mark.parametrize('input, output', test_data)
    
    def test_mbv(self, input, output):
        assert mbv(input) == output
