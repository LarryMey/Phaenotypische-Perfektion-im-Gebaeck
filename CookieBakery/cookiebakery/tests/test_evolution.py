from cookiebakery.cookies import Cookie, RecombinationCookie
from cookiebakery.cookies.evolution import Evolution
import mock

class TestEvolution:

    def setup_method(self, method):
        self.evolution = Evolution()

    def test_init(self):
        assert isinstance(self.evolution, Evolution)

    def test_discontinue_step(self):
        self.evolution.next(self.evolution.ancestors[1].last())
        assert self.evolution.ancestors[0].discontinued

    def test_recreate_step(self):
        self.evolution.next(self.evolution.ancestors[1].last())
        last_cookie = self.evolution.ancestors[0].last()
        self.evolution.next(self.evolution.ancestors[1].last())
        assert self.evolution.ancestors[0].last() is not last_cookie

    def test_recombine_step(self):
        last_cookie = self.evolution.ancestors[1].last()
        self.evolution.next(last_cookie)
        taken_cookie = self.evolution.ancestors[0].last()
        self.evolution.next(taken_cookie)
        recombined_cookie = RecombinationCookie((last_cookie, taken_cookie))
        assert  self.evolution.ancestors[0].last().properties[0] == recombined_cookie.properties[0]
        assert  self.evolution.ancestors[0].last().properties[1] == recombined_cookie.properties[1]

    @mock.patch('random.randint')
    @mock.patch('random.choice')
    def test_mutate_step(self, randint, choice):
        randint.return_value = 50
        choice.return_value = True

        self.evolution.ancestors[1].add(Cookie([50, 60]))
        self.evolution.next(self.evolution.ancestors[1].last())
        cookie = self.evolution.ancestors[1].last()
        assert cookie.properties[0] == 76
        assert cookie.properties[1] == 81

