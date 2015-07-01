from cookiebakery.graph import Graph
import random


class Cookie:

    def __init__(self, properties=list(), parents=tuple()):
        self.properties = properties
        self.parents = parents

        graph = Graph()
        graph.add(self)


def RandomCookie():
    random.seed()

    return Cookie([random.randint(0,100), random.randint(0,100)])


def MutantCookie(parent_cookie):
    random.seed()

    # we use radical functions to ensure there is a higher probability for
    # smaller mutations than for bigger ones. 

    # first, calculate parameters of radical function
    derivation_f = 6  # the lower the factor, the more derivation
    derivation_a = 100.0 / (100 ** (1.0 / derivation_f))

    mutated_properties = list()
    for prop in parent_cookie.properties:
        # get a random mutation rate, 0 -> no mutation, 100 -> huge mutation
        mutate_rate = 100 - (derivation_a * (random.randint(0,100) ** (1.0 / derivation_f)))

        # mutate
        if random.choice([True, False]):
            # mutate to positive value
            mutated_properties.append(int(prop + ((100 - prop) * mutate_rate / 100)))
        else:
            # mutate to negative value
            mutated_properties.append(int(prop - (prop * mutate_rate / 100)))

    return Cookie(mutated_properties, (parent_cookie,))


def RecombinationCookie(parent_cookies):
    recombinated_properties = list()
    for i in range(0, len(parent_cookies[0].properties)):
        recombinated_properties.append((parent_cookies[0].properties[i] + parent_cookies[1].properties[i]) / 2) # XXX

    return Cookie(recombinated_properties, parent_cookies)

