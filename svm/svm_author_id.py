#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from collections import Counter


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


clf = SVC(kernel = 'rbf' , C=10000)

to = time()
clf.fit(features_train, labels_train)
print "training time:" , round(time()-t0, 3), "s"

t1 = time()
clf.fit(freatures_test)
print "prediction time:", round(time()-t1, 3), "s"

print "accuracy:", accuracy_score(labels_test, pred)

print "Predictions:"
print "10:", pred[10]
print "26:", pred[26]
print "50:", pred[50]

c = Counter(pred)
print "No of predictions for Chris(1):", c[1]

### your code goes here ###



