from cookiebakery.cookies import Cookie
from cookiebakery.cookies.store import Store


class TestStore:

    def setup_method(self, method):
        self.store = Store()

    def test_init(self):
        assert isinstance(self.store, Store)

    def test_add_cookie(self):
        cookie = Cookie([30, 40])
        self.store.add_cookie(cookie)
        assert self.store.last_cookie() == cookie

