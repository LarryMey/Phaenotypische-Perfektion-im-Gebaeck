from cookiebakery.cookies import Cookie
from cookiebakery.cookies.ancestors import Ancestors
import mock


class TestAncestores:

    def setup_method(self, method):
        self.ancestors = Ancestors()

    @mock.patch('random.randint')
    def test_init(self, randint):
        randint.return_value = 50

        assert isinstance(self.ancestors, Ancestors)
        assert isinstance(self.ancestors.last(), Cookie)

    def test_add_cookie(self):
        cookie = Cookie([30, 40])
        self.ancestors.add(cookie)
        assert self.ancestors.last() == cookie

    def test_unset_discontinued(self):
        self.ancestors.discontinued = True
        cookie = Cookie([30, 40])
        self.ancestors.add(cookie)
        assert self.ancestors.discontinued == False

