import pickle
from pickle_vs_dill.pickle.class_source_before.example_class import example_class

a = example_class()

with open('pickle_vs_dill/pickle/object_store/example_class_object.p', 'wb') as f:
    pickle.dump(a,f)
