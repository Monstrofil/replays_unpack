#!/usr/bin/python
# coding=utf-8
from build.entities import Vehicle

__author__ = "Aleksandr Shyshatsky"


class Vehicle(Vehicle):
    def __init__(self):
        super(Vehicle, self).__init__()

    def getLearnedSkills(self):
        """
        Skill has his own skill id.
        Packed format = sum(2 ** skill_id for skill_id in skills)
        So to turn it back, we must divide number by two;
        """
        learned_skills = self.crewModifiersCompactParams['learnedSkills']
        skill_id = 1
        while learned_skills != 0:
            if learned_skills % 2 == 1:
                yield skill_id
            learned_skills /= 2
            skill_id += 1
