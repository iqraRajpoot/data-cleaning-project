# Data Cleaner

## 📌 Overview
This Python script provides a **data cleaning utility** that supports both CSV and Excel (`.xlsx`) files. It performs **essential data preprocessing tasks** such as:
✅ Handling **duplicates**  
✅ Managing **missing values**  
✅ Ensuring **data consistency**  

The cleaned dataset is then saved as a new file.

## 🚀 Features
- 🗂️ Supports **CSV** and **Excel** file formats
- 🔍 Identifies and removes **duplicate records**
- 📉 Detects and fills **missing values**
- 📊 Handles **numeric and categorical data** separately
- 💾 Saves cleaned data to a **new file**

## 🔧 Prerequisites
Ensure you have Python installed along with the required dependencies:

```sh
pip install numpy pandas openpyxl
```

## ▶️ Usage
1️⃣ Clone this repository:

```sh
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

2️⃣ Run the script:

```sh
python data_cleaner.py
```

3️⃣ Enter the dataset path and file name when prompted.

## 🏗️ Code Structure
The script contains a `data_cleaner` class that:
- 📌 Initializes with `path` and `data_name`
- 🔄 Implements `data_cleaner_func()` to:
  - ✅ **Validate** the file path and type
  - 🔎 **Identify** duplicates and missing values
  - 🛠 **Handle** missing values appropriately
  - 💾 **Save** cleaned data as a CSV file

## 📂 Example Output
After execution, the script will generate:
- 📜 `cleaned_data.csv` (**Cleaned dataset**)
- 📄 `{data_name}_duplicates.csv` (**If duplicates exist**)

## 📜 License
This project is licensed under the **MIT License** – see the LICENSE file for details.

## 🤝 Contributions
Contributions are welcome! Feel free to **open an issue** or **submit a pull request**.

---
🎯 **Happy Cleaning!** 🧹

