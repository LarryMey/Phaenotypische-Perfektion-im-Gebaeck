from cookiebakery.cookies import RandomCookie


class Ancestors:

    def __init__(self):
        self.cookies = [RandomCookie()]
        self.discontinued = False

    def add(self, cookie):
        self.cookies.append(cookie)
        self.discontinued = False

    def last(self):
        return self.cookies[-1]

    def discontinue(self):
        self.discontinued = True
