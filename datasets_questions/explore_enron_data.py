#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

keys = enron_data.keys()

countOfPoi = 0
for k in keys:
    poi = enron_data.get(k).get("poi")
    if poi == 1:
        countOfPoi += 1

print "size: ", len(enron_data)
print "values: ", enron_data.get(keys[0])
print "keys: ", keys
print "count of POI: ", countOfPoi
