import dill

with open('pickle_vs_dill/dill/object_store/example_class_object.p', 'rb') as f:
    a=dill.load(f)

print(a._name)
