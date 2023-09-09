from .constants import (
    COMMON_RESULTS,
    PLAYER_PRIVATE_RESULTS,
    INIT_ECONOMICS,
    SUBTOTAL_ECONOMICS,
    COMMON_ECONOMICS,
    CLIENT_PUBLIC_RESULTS,
    CLIENT_VEH_INTERACTION_DETAILS,
    CLIENT_BUILDING_INTERACTION_DETAILS,
    BUILDINGS_FULL_RESULTS
)


def listToDict(names, l):
    return dict(zip(names, l))


def unpackBuildinsRes(buildingsList):
    return listToDict(BUILDINGS_FULL_RESULTS, buildingsList)


def unpackCommonRes(commonResults):
    return listToDict(COMMON_RESULTS, commonResults)


def unpackPlayerPrivateRes(privateList):
    result = listToDict(PLAYER_PRIVATE_RESULTS, privateList)

    result['init_economics'] = listToDict(INIT_ECONOMICS, result['init_economics'])
    result['common_economics'] = listToDict(COMMON_ECONOMICS, result['common_economics'])
    result['subtotal_economics'] = listToDict(SUBTOTAL_ECONOMICS, result['subtotal_economics'])
    return result


def unpackClientPublicRes(publicList):
    result = listToDict(CLIENT_PUBLIC_RESULTS, publicList)

    result['interactions'] = {
        targetId: listToDict(CLIENT_VEH_INTERACTION_DETAILS, data)
        for targetId, data in result['interactions'].items()
    }
    result['buildingInteractions'] = {
        targetId: listToDict(CLIENT_BUILDING_INTERACTION_DETAILS, data)
        for targetId, data in result['buildingInteractions'].items()
    }

    return result