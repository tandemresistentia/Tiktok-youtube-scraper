#Delete
import os
import os.path

for dirpath, dirnames, filenames in os.walk("."):
    for filename in [f for f in filenames if f.endswith(".mp4")]:
        os.remove(os.path.join(dirpath, filename))

for dirpath, dirnames, filenames in os.walk("."):
    for filename in [f for f in filenames if f.endswith(".ts")]:
        os.remove(os.path.join(dirpath, filename))