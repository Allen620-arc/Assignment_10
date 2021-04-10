"""
    Name: Allen Keettikkal
    NSID: alk423
    Student Number: 11278995
    Instructor: Jeffrey Long
"""

import LocationNode as LN


class MobilityProfile(object):
    def __init__(self, aList=None):
        """
        Purpose: creates a mobility profile. If no aList is given, profile is set to None
        Pre-condition:
            aList: A list of five strings, showing the sequential locations that the user had visited.
        Post-condition: A mobility profile is created
        Return: None
        """
        if aList is None:
            self.profile = None
        else:
            self.create_profile(aList)

    def create_profile(self, aList):
        """
        Purpose:
            Creates a mobility profile using the given aList
        Pre-conditions:
            aList: A list of five strings, showing the sequential locations that the user had visited.
            aList should only have five locations.
        Post-condition:
            A mobility profile is created
        Return: None
        """
        node_1 = LN.LocationNode()
        node_2 = LN.LocationNode()
        node_3 = LN.LocationNode()
        node_4 = LN.LocationNode()
        node_5 = LN.LocationNode()
        node_1.set_data(aList[0])
        node_2.set_data(aList[1])
        node_1.set_next(node_2)
        node_3.set_data(aList[2])
        node_2.set_next(node_3)
        node_4.set_data(aList[3])
        node_3.set_next(node_4)
        node_5.set_data(aList[4])
        node_4.set_next(node_5)
        self.profile = node_1

    def compare_profile(self, otherProfile):
        """
        Purpose:
            Compare two mobility profiles. Return True when the two mobility profile as a location matched.
        Pre-conditions:
            otherProfile: Another user's mobility profile for comparison.
            Both self and other profiles must not be None.
        Post-condition:
            None
        Return: True if there is a match, False for otherwise.
        """
        if self.profile.get_current_location() == otherProfile.profile.get_current_location():
            return True
        else:
            while self.profile is not None or otherProfile.profile is not None:
                if self.profile.get_next_location() == otherProfile.profile.get_next_location():
                    return True
                self.profile = self.profile.get_next_location()
                otherProfile.profile = otherProfile.profile.get_next_location()
            return False
