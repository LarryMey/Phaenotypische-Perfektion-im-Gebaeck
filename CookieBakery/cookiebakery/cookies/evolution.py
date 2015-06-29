from cookiebakery.cookies import MutantCookie, RecombinationCookie
from cookiebakery.cookies.ancestors import Ancestors


class Evolution:

    last_cookie = None

    def __init__(self):
        self.ancestors = [Ancestors(), Ancestors()]

    def next(self, taken_cookie):
        for i, anc in enumerate(self.ancestors):
            if taken_cookie is anc.last():
                if anc.discontinued:
                    anc.add(RecombinationCookie((self.last_cookie, taken_cookie)))
                else:
                    anc.add(MutantCookie(taken_cookie))
            else:
                if anc.discontinued:
                    # start a new ancestor line
                    self.ancestors[i] = Ancestors()
                else:
                    # last chance for ancestor line
                    anc.discontinue()

        self.last_cookie = taken_cookie
