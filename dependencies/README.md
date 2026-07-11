# 📂 Task Automation Tool

## 📌 Project Overview

The **Task Automation Tool** is a Python application that automatically organizes files into folders based on their file type. It helps users keep their directories clean by sorting files into categories such as Images, Documents, Videos, Music, Archives, Programs, and Others.

---

## 🎯 Features

- Automatically organizes files by extension.
- Creates folders if they do not already exist.
- Supports multiple file categories.
- Handles unknown file types by moving them to the **Others** folder.
- Easy to use through the command line.
- Uses only Python's built-in libraries.

---

## 🛠️ Technologies Used

- Python 3.x
- os module
- shutil module

---

## 📁 Project Structure

```
Task_Automation_Tool/
│── main.py
│── organizer.py
│── config.py
│── utils.py
│── requirements.txt
│── README.md
│── .gitignore
│── sample_files/
│── output/
└── screenshots/
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YourUsername/Task_Automation_Tool.git
```

### 2. Open the project

```bash
cd Task_Automation_Tool
```

### 3. Run the program

```bash
python main.py
```

### 4. Enter the folder path when prompted.

Example:

```
C:\Users\YourName\Desktop\sample_files
```

---

## 📂 Supported File Types

| Category | Extensions |
|----------|------------|
| Images | .jpg, .jpeg, .png, .gif, .bmp |
| Documents | .pdf, .doc, .docx, .txt, .pptx, .xlsx |
| Videos | .mp4, .avi, .mkv, .mov |
| Music | .mp3, .wav, .aac |
| Archives | .zip, .rar, .7z |
| Programs | .exe, .msi |

---

## 📸 Sample Output

```
Moved: image.jpg → Images
Moved: report.pdf → Documents
Moved: song.mp3 → Music
Moved: video.mp4 → Videos

Task Completed Successfully!
```

---

## 🚀 Future Enhancements

- Graphical User Interface (GUI)
- Drag-and-drop folder selection
- Automatic folder monitoring
- File duplicate detection
- Logging and report generation

---

## 👩‍💻 Author

**Thanuja Reddy**

Final Year B.E. Electronics and Communication Engineering (ECE)

---

## 📜 License

This project is created for learning and internship purposes.