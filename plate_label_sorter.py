import os
import shutil
import re


source_folder = r"D:\plate_data\plate_data"
output_folder = r"D:\plate_data\sorted"


os.makedirs(output_folder, exist_ok=True)


for image_name in os.listdir(source_folder):

    if not image_name.lower().endswith(".jpg"):
        continue


    match = re.search(r'\d+([a-zA-Z]+)\d+', image_name)


    if match:
        label = match.group(1)

    else:
        print("Label پیدا نشد:", image_name)
        continue


    label_folder = os.path.join(output_folder, label)

    os.makedirs(label_folder, exist_ok=True)


    source_path = os.path.join(source_folder, image_name)

    destination_path = os.path.join(label_folder, image_name)


    shutil.copy(source_path, destination_path)


    print(image_name, "---->", label)


print("**************************************************************")
print("\n number of pictures of classes : ")


for class_name in sorted(os.listdir(output_folder)):

    class_path = os.path.join(output_folder, class_name)

    if os.path.isdir(class_path):

        count = len([
            img for img in os.listdir(class_path)
            if img.lower().endswith(".jpg")
        ])

        print(f"کلاس {class_name}: {count} عکس")


print("\nDone :))")