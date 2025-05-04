Perfect — based on your setup (Docker, Jupyter, Label Studio, YOLOv8n), here’s your customized **Table of Contents** for the full pipeline from labeling to training and improving a stingless bee detection model:

---

## 🐝 Bee Detection Pipeline: Table of Contents

### 🧩 **Module 1: Label Studio**

* 1.1 Set up Label Studio inside Docker
* 1.2 Create project with `"stingless_bee"` label
* 1.3 Upload and organize images
* 1.4 Annotate with bounding boxes
* 1.5 Export YOLO-format labels

---

### 🧠 **Module 2: YOLOv8n (Bee Detection Setup)**

* 2.1 Install Ultralytics inside Docker or Jupyter
* 2.2 Understand dataset.yaml format
* 2.3 Organize dataset: `images/train`, `images/val`, `labels/train`, etc.
* 2.4 Link Label Studio export to YOLO format

---

### 🏋️‍♂️ **Module 3: Train Model**

* 3.1 Run training with `yolo task=detect ...`
* 3.2 Use MacBook M1 with MPS backend
* 3.3 Monitor training inside Jupyter
* 3.4 Save and version model weights

---

### 🔍 **Module 4: Test Model**

* 4.1 Load trained `.pt` model
* 4.2 Run inference on test images
* 4.3 Visualize bounding boxes + bee count
* 4.4 Compare with manual annotations

---

### 📊 **Module 5: Evaluate Model**

* 5.1 Use `mAP@0.5`, precision, recall
* 5.2 Track confusion matrix
* 5.3 Keep evaluation set fixed (do not train on it)
* 5.4 Log phase performance

---

### ♻️ **Module 6: Improve Model**

* 6.1 Add more data (v2, v3, etc.)
* 6.2 Clean label noise or reannotate
* 6.3 Apply augmentation (blur, zoom, rotate)
* 6.4 Use smaller or larger YOLOv8 models (n → s)

---

### 📘 **Module 7: Log Model Changes**

* 7.1 Track training changes (epochs, image size, model type)
* 7.2 Version datasets (v1, v2...)
* 7.3 Save YAML config + training logs
* 7.4 Maintain model changelog in `model_log.md`

---

Would you like to begin with **Module 1: Label Studio – Export YOLO Labels** now?
