

---

## 📁 Let's Start Module 11: Convert CSV to YOLO Format

You already have:
```csv
filename,x,y,w,h,label
ball_1.jpg,173,22,149,178,ball
```

YOLO format (per image in `.txt`) should look like this:
```
0 0.422 0.422 0.364 0.436
```

Which means:
```
[class_id] [x_center] [y_center] [width] [height]   # All normalized (0-1)
```

---

## 🛠 Code to Convert `ball_labels.csv` → YOLO TXT format

```python
import os
import pandas as pd
import cv2

# Load metadata
df = pd.read_csv("ball_labels.csv")

# Map label to class ID (e.g., "ball" = 0)
label_to_id = {"ball": 0}

# Folder where images are stored
image_dir = "dataset/ball"
labels_dir = "dataset/ball/labels"
os.makedirs(labels_dir, exist_ok=True)

# Loop through metadata rows
for _, row in df.iterrows():
    filename = row['filename']
    label = row['label']
    class_id = label_to_id[label]

    # Load image to get width and height
    image_path = os.path.join(image_dir, filename)
    img = cv2.imread(image_path)
    h, w = img.shape[:2]

    # Convert bbox to YOLO format
    x_center = (row['x'] + row['w'] / 2) / w
    y_center = (row['y'] + row['h'] / 2) / h
    width = row['w'] / w
    height = row['h'] / h

    # Write to TXT file (one per image)
    txt_filename = os.path.splitext(filename)[0] + ".txt"
    txt_path = os.path.join(labels_dir, txt_filename)
    with open(txt_path, 'w') as f:
        f.write(f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n")
```

---

### ✅ After Running:
You’ll have:
```
dataset/ball/
├── ball_1.jpg
├── ball_1.txt   ← YOLO label
├── ball_2.jpg
├── ball_2.txt
...
```

---