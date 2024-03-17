__author__ = "Aleksandr Shyshatsky"

from replay_unpack.core.unicoding import unicodize


class PlayerMode(object):
    playerModeType: int
    observedTeamId: int

    def __setstate__(self, d):
        self.__dict__ = unicodize(d)
