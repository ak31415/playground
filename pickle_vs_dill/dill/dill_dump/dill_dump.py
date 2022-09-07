import dill
from pickle_vs_dill.dill.class_source_before.example_class import example_class

a = example_class()

with open('pickle_vs_dill/dill/object_store/example_class_object.p', 'wb') as f:
    dill.dump(a,f,byref=False)


#https://stackoverflow.com/questions/32363312/why-dill-dumps-external-classes-by-reference-no-matter-what