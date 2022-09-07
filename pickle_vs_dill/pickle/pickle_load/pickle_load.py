import pickle

with open('pickle_vs_dill/pickle/object_store/example_class_object.p', 'rb') as f:
    a=pickle.load(f)

print(a._name)
