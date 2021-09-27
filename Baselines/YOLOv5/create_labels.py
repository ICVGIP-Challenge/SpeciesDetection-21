import json
import os

# PATH to the train and validation labels in JSON format
train_json_path = "../../dataset/labels/train.json"
valid_json_path = "../../dataset/labels/validation.json"


# class xcentre ycentre width height  <-- normalised values
def bbox_to_yolo(bbox, width, heigth):
    if len(bbox) == 0:
        return "0.5 0.5 0.9999 0.9999"
    x_centre = str((bbox[0] + bbox[2]) / (2 * width))
    y_centre = str((bbox[1] + bbox[3]) / (2 * heigth))
    wi = str(bbox[2] / width)
    hi = str(bbox[3] / heigth)
    return x_centre + " " + y_centre + " " + wi + " " + hi


if __name__ == "__main__":
    confirmation = "x"
    for ty in (['train', 'validation']):
        if ty == 'train':
            path = "../../dataset/labels/train/"  # update the path where the training labels txt files will be saved
            f = open(train_json_path)
        else:
            path = "../../dataset/labels/validation/"  # update the path where the validation labels txt files will be saved
            f = open(valid_json_path)

        if os.path.isdir(path) and confirmation != "y":
            confirmation = input("Path '%s" %path + "' already exists. Overwrite? (y/n)")
            if confirmation == "n":
                break
        elif not os.path.isdir(path):
            os.mkdir(path)

        print("Transforming %s" %ty, "labels!")


        check_set = set()
        training_data = json.load(f)

        for i, ann in enumerate(training_data["annotations"]):
            image_id = str(ann["image_id"])
            category_id = str(ann["category_id"])
            bbox = ann['bbox']  # "bbox": [x,y,width,height]

            imag = training_data['images'][i]
            file_path = imag['file_path'].split("/")[-1][:-4]
            heigth = imag['height']
            width = imag['width']

            file_name = path + file_path + ".txt"

            content = category_id + " " + bbox_to_yolo(bbox, width, heigth)
            if image_id in check_set:
                file = open(file_name, "a")
                file.write("\n")
                file.write(content)
                file.close()
            else:
                check_set.add(image_id)
                file = open(file_name, "w")
                file.write(content)
                file.close()
