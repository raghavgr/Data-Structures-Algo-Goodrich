"""
Calculates the number of bytes used by a file/folder
and any descendants.
"""

import os

def disk_usage(path):
    """
    return number of bytes used by file/folder at the path
    """
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)        # complete the full path
            total += disk_usage(childpath)                  # calculate childpath's disk usage
    print('{0:<7}'.format(total), path)
    return total
