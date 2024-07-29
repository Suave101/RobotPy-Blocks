import inspect
import json

import wpilib


def recursivelyMembersForClasses(library):
    libraryMemberList = inspect.getmembers(library)
    dataMap = []
    # For all items in Class
    for member in libraryMemberList:
        # If item in class is a class add to list of subclasses
        if inspect.isclass(member[1]) and str(type(member[1])) != "<class 'type'>":
            containsSubclasses = True
            # Is a Class | Subclass Name | Map of Subclass
            dataMap.append([
                True,
                member[0],
                {
                    "Docstring": inspect.getdoc(member[1]),
                    "Variables": str(member[1].__dict__.items())
                },
                recursivelyMembersForClasses(member[1])
            ])
        else:
            if member[0][0] != "_":
                try:
                    dataMap.append(
                        [False, member[0],
                         {
                             "Args": inspect.getfullargspec(member[1]).args,
                             "Defaults": inspect.getfullargspec(member[1]).defaults,
                             "Docstring": inspect.getdoc(member[1])
                         }
                         ])
                except:
                    pass
    if not dataMap:
        return None
    else:
        return dataMap

file = open("data.json", "w")
file.write(json.dumps(recursivelyMembersForClasses(wpilib), indent=5))
file.close()
