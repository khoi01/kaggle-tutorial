Perfect — let’s dive into your **Module 6: Improve Model**, and I’ll include a v2 checklist to guide your next training round based on what v1 taught you.

---

## ♻️ **Module 6: Improve Model** (Concept + Checklist)

---

### ✅ **6.1 Add More Data (v2, v3, etc.)**

#### 🔹 Concept:

* v1 had only 8 images — not enough for bees with varied backgrounds and sizes.
* You need 30–100+ well-labeled images to improve performance significantly.

#### ✅ Action:

* Create a new folder: `datasets/v2/raw/`
* Collect more images: mirrorless + close-up + GoPro + phone
* Cover different conditions: lighting, bee sizes, entrance types

#### 🧠 Bee Detection v2 Data Checklist:

| ✅ Must-Have            | Description                        |
| ---------------------- | ---------------------------------- |
| ✅ 30+ images           | Ideally 50–200 for training        |
| ✅ Mixed quality        | Include blurry and sharp           |
| ✅ Different angles     | Overhead, side, zoomed out/in      |
| ✅ Visible bees & empty | Balance both for contrast learning |
| ✅ Partial bee samples  | Helps model learn real-world crops |

---

### ✅ **6.2 Clean Label Noise or Reannotate**

#### 🔹 Concept:

* Bad or inconsistent labels = worse than no labels
* Label Studio must:

  * Use `"stingless_bee"` only
  * Have bounding boxes that are tight and centered

#### ✅ Action:

* Use Label Studio to **review existing labels** in v1 and v2
* Remove images where bees are unrecognizable
* Ensure every bee visible = labeled

---

### ✅ **6.3 Apply Augmentation (blur, zoom, rotate)**

#### 🔹 Concept:

* Augmentations synthetically increase dataset size and improve robustness
* Helps with small datasets and overfitting

#### ✅ Tools:

* Use YOLOv8 built-in augmentations (enabled by default)
* Or apply custom augmentations using Albumentations before training

#### 🧠 Useful Augmentations:

| Technique           | Effect                        |
| ------------------- | ----------------------------- |
| Random blur         | Helps with low focus          |
| Horizontal flip     | Natural camera angle sim      |
| Brightness/contrast | Handles lighting changes      |
| Random zoom         | Teaches to detect small bees  |
| Random crop         | Forces model to rely on parts |

---

### ✅ **6.4 Try Smaller or Larger YOLOv8 Models**

#### 🔹 Concept:

* `yolov8n.pt` = very fast but may underfit
* `yolov8s.pt` = better accuracy (still M1-friendly)

#### ✅ Recommendation:

```python
model = YOLO('yolov8s.pt')  # small model
```

> ⚠️ Needs more RAM/GPU time — test on M1 before committing.

---

## 🧠 Suggested Folder Structure (v2)

```
datasets/
└── v2/
    ├── raw/
    ├── labels_raw/
    ├── images/
    │   ├── train/
    │   └── val/
    ├── labels/
    │   ├── train/
    │   └── val/
    └── dataset.yaml
```

Then re-train:

```python
model.train(data="datasets/v2/dataset.yaml", epochs=100, imgsz=640)
```

---

Would you like me to:

* Generate a clean `model_log.csv` entry template for v2?
* Or give you a checklist notebook for dataset QA before retraining?
