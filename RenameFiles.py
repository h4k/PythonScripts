
import os

path = "D:\\#Test"

i = 0
target = 10

while i < target: 
    os.path
    f = open(os.path.join(path, "test_" + str(i)) + "test_", "w+")
    f.close()
    print(f.name)
    i = i +1

print("Creating done.")

for filename in os.listdir(path):
    if "test_" in filename:
        try:
            os.rename(os.path.join(path, filename), os.path.join(path, filename.replace("test_", "")))
            print("found - " + filename)
        except Exception as e:
            print("found but error - " + filename + " - " + str(e))
            pass
    else:
        continue

print("Renaming done.")
