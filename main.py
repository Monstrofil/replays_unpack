from custom_replay_parser import CustomReplayParser
from random import randint
from random import shuffle

from replay_unpack import Unknown

if __name__ == '__main__':
    obj = CustomReplayParser("replays/826_1541979799_20181111_171508_PASB017-Montana-1945_44_Path_warrior.wowsreplay")
    # pac = filter(lambda x:'unknown' in str(type(x.data)).lower() ,obj.packets)
    # types = set(map(lambda x:x.type,pac))
    # types.remove(14)
    # types.remove(24)
    #
    #
    #
    # with open('G:\\Python\\replays_unpack\\Orlan_34_OC_islands.txt','w') as f:
    #     for type in types:
    #         type_pacs = filter(lambda x:x.type == type,pac)
    #         type_pacs = map(lambda x: x.data.value + ' ' + str(x.time), type_pacs)
    #         f.write('================' + str(type) + '================\r')
    #         for item in type_pacs:
    #             f.write(str(item) + '\n')
    # pacs = filter(lambda x: x.type == 43, obj.packets)
    # pacs = list(filter(lambda x: x.data.id1 == (28648,), pacs))
    # shuffle(pacs)
    # pacs = pacs[:int(len(pacs) / 4.0)]
    #
    # opacs = list(filter(lambda x: x.type == 10, obj.packets))
    # shuffle(opacs)
    # opacs = opacs[:int(len(opacs) / 3.0)]
    #
    # pacs = pacs + opacs
    # shuffle(pacs)
    #
    # import matplotlib.pyplot as plt
    # from colour import Color
    #
    # red = Color("red")
    # colorList = list(red.range_to(Color("blue"), int(max(map(lambda x: x.time, pacs)) + 1)))
    #
    # for i in range(len(pacs)):
    #     pac = pacs[i]
    #     plt.plot(pac.data.position.x, pac.data.position.z, color=colorList[int(pac.time)].get_rgb(), marker='o',
    #              markersize=1)
    #     print str(int(float(i) / len(pacs) * 100)) + '%'

    pac = filter(lambda x: isinstance(x.data, Unknown), obj.packets)
    types = set(map(lambda x: x.type, pac))
    with open('record.txt', 'w') as f:
        for type in types:
            type_pacs = filter(lambda x: x.type == type, pac)
            type_pacs = map(lambda x: x.data.value + ' ' + str(x.time), type_pacs)
            f.write('================' + str(type) + '================\r')
            for item in type_pacs:
                f.write(str(item) + '\n')

    # plt.xlabel('x')
    #
    # plt.ylabel('y')
    #
    # plt.axis('equal')
    # # plt.ylim(-800, 800)
    # # plt.xlim(-800, 800)
    #
    # plt.title('positions')
    # plt.grid(True)
    # plt.show()
    #
    # #
    # # plt.xlabel('time')
    # #
    # # plt.ylabel('value')
    # #
    # #
    # # plt.title('angles')
    # # plt.grid(True)
    # # plt.show()
    # pass
