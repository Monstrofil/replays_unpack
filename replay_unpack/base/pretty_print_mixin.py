# coding=utf-8


class PrettyPrintObjectMixin(object):
    def __repr__(self):
        if self.__slots__:
            props = {k: getattr(self, k) for k in self.__slots__}
        else:
            props = self.__dict__
        return "<{}>: {}".format(self.__class__.__name__, props)
