from cookiebakery.cookies import Cookie, MutantCookie, RandomCookie, RecombinationCookie
import mock

class TestCookie:

    def test_init(self):
        cookie = Cookie([50, 60])
        assert isinstance(cookie, Cookie)
        assert cookie.properties[0] == 50
        assert cookie.properties[1] == 60

    @mock.patch('random.randint')
    def test_random_cookie(self, randint):
        randint.return_value = 50

        cookie = RandomCookie()
        assert cookie.properties[0] == 50
        assert cookie.properties[1] == 50

    @mock.patch('random.randint')
    @mock.patch('random.choice')
    def test_mutant_cookie(self, randint, choice):
        randint.return_value = 50
        choice.return_value = True

        parent_cookie = Cookie([50, 60])
        cookie = MutantCookie(parent_cookie)
        assert cookie.properties[0] == 76
        assert cookie.properties[1] == 81

    def test_remobination_cookie(self):
        mother_cookie = Cookie([40, 80])
        father_cookie = Cookie([60, 40])

        cookie = RecombinationCookie((mother_cookie, father_cookie))
        assert cookie.properties[0] == 50
        assert cookie.properties[1] == 60
