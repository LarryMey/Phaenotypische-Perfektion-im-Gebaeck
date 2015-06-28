class Store:

    cookies = []

    def add_cookie(self, cookie):
        self.cookies.append(cookie)

    def last_cookie(self):
        return self.cookies[-1]
