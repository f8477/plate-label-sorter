import os
import shutil
import re


source_folder = r"C:\Users\cactus.pc\Desktop\plate_label_sorter\plate_data\plate_data"
output_folder = r"C:\Users\cactus.pc\Desktop\plate_label_sorter\sorted"


os.makedirs(output_folder, exist_ok=True)
total_input = len(os.listdir(source_folder))
print("Total input files:", total_input)

for image_name in os.listdir(source_folder):

    if not image_name.lower().endswith(".jpg"):
        continue


    match = re.search(r'\d+([a-zA-Z]+)\d+', image_name)

    if match:
        label = match.group(1)

    elif "-" in image_name or "_" in image_name:
        label = "-"

    else:
        label = "none"


    if label == "sat":
        new_label = "sad"

    elif label == "th":
        new_label = "c"

    elif label == "ghgh":
        new_label = "gh"

    else:
        new_label = label



    label_folder = os.path.join(output_folder, new_label)

    os.makedirs(label_folder, exist_ok=True)



    new_image_name = image_name.replace(label, new_label)


    source_path = os.path.join(source_folder, image_name)

    destination_path = os.path.join(label_folder, new_image_name)

    # overwrite
    if os.path.exists(destination_path):

        name, ext = os.path.splitext(new_image_name)

        counter = 1

        while os.path.exists(destination_path):
            new_image_name = f"{name}_{counter}{ext}"
            destination_path = os.path.join(label_folder, new_image_name)
            counter += 1


    shutil.copy(source_path, destination_path)


    print(image_name, "---->", new_label)



print("**************************************************************")
print("\n number of pictures of classes : ")


for class_name in sorted(os.listdir(output_folder)):

    class_path = os.path.join(output_folder, class_name)

    if os.path.isdir(class_path):

        count = len([
            img for img in os.listdir(class_path)
            if os.path.isfile(os.path.join(class_path, img))
        ])

        print(f"class {class_name}: {count} picture")


print("\nChecking total output images...")
total_output = 0

for root, dirs, files in os.walk(output_folder):
    for file in files:
        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            total_output += 1


print("Total output images:", total_output)

print("\nDone :))")