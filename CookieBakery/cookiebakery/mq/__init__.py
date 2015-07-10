from threading import Thread
import logging
import zmq

class CookiePublisher(object):

    # there is only one publisher, so implement as singleton
    class __CookiePublisher__:
        def __init__(self):
            context = zmq.Context()
            self.publisher = context.socket(zmq.PUB)
            self.publisher.bind("tcp://*:9000")
            logging.debug("initialized CookiePublisher")

        def publish(self, cookie):
            parents = list(map(lambda x: id(x), cookie.parents))
            message = (dict(cid=id(cookie), parents=parents))
            self.publisher.send_json(message)
            logging.info("published new cookie {}".format(id(cookie)))

    __instance__ = None

    def __new__(cls):
        if not CookiePublisher.__instance__:
            CookiePublisher.__instance__ = CookiePublisher.__CookiePublisher__()
        return CookiePublisher.__instance__

    def __getattr__(self, name):
        return getattr(self.__instance__, name)

    def __setattr__(self, name):
        return setattr(self.__instance__, name)


class CookieRecvr(Thread):

    __continue__ = True

    def __init__(self, listener):
        Thread.__init__(self)
        self.daemon = True
        self.listener = listener

        context = zmq.Context()
        self.subscriber = context.socket(zmq.SUB)
        self.subscriber.connect("tcp://127.0.0.1:9000")
        self.subscriber.setsockopt_string(zmq.SUBSCRIBE, '')
        self.subscriber.setsockopt(zmq.RCVTIMEO, 120000)

    def run(self):
        logging.debug('starting cookie subscription')
        while self.__continue__:
            try:
                message = self.subscriber.recv_json()
                logging.info('recived new cookie')
                self.listener.new_cookie(message)
            except Exception as e:
                logging.error(e)
                raise e

    def stop(self):
        self.__continue__ = False
        self.subscriber.close()
        logging.debug('stopping cookie subscription')
