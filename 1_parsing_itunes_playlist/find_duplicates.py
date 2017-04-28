# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 13:56:36 2017

@author: hschoonjans
"""

import plistlib

#  finding duplicate tracks with the findDuplicates()
def find_duplicates(file_name):
    with open(file_name, 'rb') as fp:
        pl = plistlib.load(fp) # readPlist is deprecated...
    tracks = pl["Tracks"]
    track_names = {}
    duplicates = []
    
    for track_id, track in tracks.items():
        #try:
        name = track["Name"]
        duration = track["Total Time"]
        duration_seconds = duration//1000
        duration_str = str(duration_seconds)
        
        if not name in track_names.keys():
            track_names[name] = {}
            track_names[name][duration_str] = 1
        elif not duration_str in track_names[name].keys():
            track_names[name][duration_str] = 1
        else:
            track_names[name][duration_str] = track_names[name][duration_str] + 1
            duplicates.append(name)
        #except:
        #    pass
    
    # prints the names of the duplicate titles.
    print(set(duplicates))
    
find_duplicates("test-data/mymusic.xml")
