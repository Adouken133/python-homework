import os

for root, dirs, files in os.walk(r"C:\Users\01yt0\Desktop", topdown=False):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))
      

