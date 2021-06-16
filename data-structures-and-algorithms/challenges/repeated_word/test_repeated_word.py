import pytest

from challenges.repeated_word.repeated_word import repeated_word as rw


class TestRepeatedWord:
    def test_proof_of_life(self):
        assert rw

    def test_type_error(self):
        with pytest.raises(TypeError) as err:
            assert rw(4)
        assert str(err.value) == 'text must be a string!'

    test_data = (
        ("Once upon a time, there was a brave princess who...",	"a"),
        ("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...",	"it"),
        ("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...",	"summer"),
        ('All unique words', None),
    )

    @pytest.mark.parametrize('input, output', test_data)
    def test_rw_pass(self, input, output):
        assert rw(input) == output
