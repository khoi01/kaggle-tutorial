### 📂 4. Track Dataset with `dvc add`

Let’s say you have a folder of bee images you want to version:

```
/app/data/raw/
  ├── img001.jpg
  ├── img002.jpg
  └── ...
```

---

### ✅ Step-by-Step

1. **Create the folder and add images** (you can also just add a few dummy images for now):

   ```bash
   mkdir -p data/raw
   echo "dummy" > data/raw/img001.jpg
   echo "dummy" > data/raw/img002.jpg
   ```

2. **Track the folder with DVC**:

   ```bash
   dvc add data/raw
   ```

   ✅ Output:

   ```
   Adding...
   └── data/raw.dvc
   ```

3. **Check files:**

   * `data/raw/` stays in your filesystem (but is Git-ignored).
   * `data/raw.dvc` is a small text file that tracks hash, size, etc.

4. **Track the `.dvc` file in Git:**

   ```bash
   git add data/raw.dvc .gitignore
   git commit -m "Track raw dataset with DVC"
   ```

---

### 📌 Summary

| File/Folder    | Purpose                                    |
| -------------- | ------------------------------------------ |
| `data/raw/`    | Your real dataset (not committed to Git)   |
| `data/raw.dvc` | Pointer file tracked by Git                |
| `.dvc/`        | Internal metadata (like `.git/`)           |
| `.gitignore`   | Automatically updated to ignore large data |

---

Ready for **Step 5: Configure Google Drive remote** so you can sync this dataset to the cloud?
