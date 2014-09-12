import os
root = os.path.dirname(os.path.abspath(__file__))
print root
print os.path.split(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])[0]
