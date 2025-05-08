# 🐝 Stingless Bee Detection Dataset Setup (YOLOv8 + Label Studio)

## 🔹 Step 1: Prepare Folder Structure

1.1 Create a new folder named `datasets/v1` inside your project.  
1.2 Inside the `v1` folder, create the following subfolders:
- `images`
- `labels`
- `labels_raw`
- `raw`

1.3 Inside the `images` folder, create:
- `train`
- `val`

1.4 Inside the `labels` folder, create:
- `train`
- `val`

1.5 Add the raw images (to be labeled) into the `raw` folder.

---

## 🔹 Step 2: Label Images Using Label Studio

2.1 Run Label Studio.  
2.2 Create a new project and name it (e.g., "Stingless Bee Detection").  
2.3 Upload images by selecting them from the `raw` folder and begin annotating each image using the `"stingless_bee"` label.  
2.4 After labeling, export the dataset in **YOLO format**.

---

## 🔹 Step 3: Process YOLO Labels

3.1 Move the exported YOLO `.txt` annotation files into the `labels_raw` folder.  
3.2 Open and run the notebook **`1.Split Between raw and labels_raw into Images and Labels.ipynb`**  
&nbsp;&nbsp;&nbsp;&nbsp;This notebook splits the data into 80% training and 20% validation.  
3.3 Open and run the notebook **`2.Validate Split Process.ipynb`**  
&nbsp;&nbsp;&nbsp;&nbsp;This checks if all images have matching labels and if the split was successful.

---

✅ You are now ready to train your YOLOv8 model using this dataset.


## 🔹 Step 4: Check File Existed
4.1 Go to root folder, open and run the notebook **`3.Check File Existed.ipynb`**, it anything is okey then its on the wring position.
4.2 dataset.yaml is most crucial part make sure everything in order.


