import inspect
import pybind11
import json
import wpilib


def parseMembersForClasses(library):
    libraryMemberList = inspect.getmembers(library)
    for member in libraryMemberList:
        if str(type(member[1])) == "<class 'pybind11_builtins.pybind11_type'>":
            print(member[0])


# print(parseMembersForClasses(wpilib))
parseMembersForClasses(wpilib)
