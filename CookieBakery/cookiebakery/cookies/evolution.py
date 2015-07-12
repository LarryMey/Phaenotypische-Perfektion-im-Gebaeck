from cookiebakery.cookies import MutantCookie, RecombinationCookie
from cookiebakery.cookies.ancestors import Ancestors


class Evolution:

    def __init__(self):
        self.last_cookie = None
        self.visits = list()
        self.ancestors = [Ancestors(), Ancestors()]

    def register(self, func):
        if func not in self.visits:
            self.visits.append(func)

    def next(self, taken_cookie):
        new_ancestor = None
        for i, anc in enumerate(self.ancestors):
            if taken_cookie is anc.last():
                if anc.discontinued:
                    new_cookie = RecombinationCookie(
                        (self.last_cookie, taken_cookie))
                else:
                    new_cookie = MutantCookie(taken_cookie)
                anc.add(new_cookie)
            else:
                if anc.discontinued:
                    # start a new ancestor line
                    new_ancestor = i
                    self.ancestors[i] = Ancestors()
                else:
                    # last chance for ancestor line
                    anc.discontinue()

        self.last_cookie = taken_cookie
        for func in self.visits:
            if new_ancestor != None:
                func(new_cookie, self.ancestors[new_ancestor].last())
            else:
                func(new_cookie)
