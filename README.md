# FacePass: Facial Recognition Employee Entry System  
*A modern system for employee entry management using facial recognition, real-time processing, and a cloud-first database.*

---

## 📌 Overview  
**FacePass** is a facial recognition system designed to streamline employee entry management. It includes:  
- **Admin Dashboard**: Add/remove employees, manage face encodings, and view logs (built with Streamlit/Gradio).  
- **End-User Interface**: Real-time face detection and entry logging via OpenCV.  
- **Cloud Database**: Securely store employee data and logs using Supabase.  

Built with privacy and scalability in mind, this system replaces manual check-ins with AI-powered automation.  

---

## 🚀 Key Features  
- **Real-Time Face Recognition**: Low-latency processing with OpenCV and `face_recognition` library.  
- **Admin Dashboard**:  
  - Add/remove employees with face encodings.  
  - View/modify Supabase records.  
  - Export entry logs by date or department.  
- **Entry Logging**: Automatic timestamped logging into Supabase.  
- **Modular Architecture**: Separate services for admin, recognition, and database.  

---

## 🧩 System Architecture  

### Components  
1. **Admin Dashboard** (Streamlit):  
   - Manage employee face encodings and Supabase data.  
   - Visualize entry logs with filters.  
2. **Recognition Service** (Python/OpenCV):  
   - Captures video stream and runs face detection.  
   - Compares embeddings with Supabase-stored encodings.  
3. **Supabase Database**:  
   - Stores `employees` (name, face_encoding), `entry_logs`, and `visitors`.  

---

## ⚙️ Installation  
### Prerequisites  
- Python 3.8+  
- Supabase account (for cloud DB)  

```bash  
# Clone the repo  
git clone https://github.com/yourusername/FacePass.git  
cd FacePass  

# Install dependencies  
pip install -r requirements.txt  
```

---

## 🛠️ Usage  
### 1. Admin Dashboard (Streamlit)  
```bash  
streamlit run admin_dashboard.py  
```  
**Features**:  
- Upload employee photos to generate face encodings.  
- Delete entries or filter logs by date.  
- Directly query Supabase tables.  

### 2. Recognition Service  
```bash  
python recognition_service.py  
```  
- Uses webcam to detect faces and log entries in real time.  
- Matches faces against Supabase `face_encodings` with configurable tolerance.  

---

## 🔧 Configuration  
### Supabase Setup  
1. Create a `.env` file:  
```env  
SUPABASE_URL=your-supabase-url  
SUPABASE_KEY=your-anon-key  
```  

2. Initialize tables using `supabase_init.sql`.  

### Face Recognition Settings  
- Adjust `TOLERANCE` in `config.py` for stricter/looser face matching.  
- Enable GPU acceleration (if available) in `recognition_service.py`.  

---

## 🛠️ Tech Stack  
| Component               | Tools/Libraries                                   |  
|-------------------------|---------------------------------------------------|  
| **Face Recognition**    | `face_recognition` (Dlib), OpenCV                 |  
| **Admin Dashboard**     | Streamlit                                         |  
| **Database**            | Supabase (PostgreSQL)                             |  
| **Backend**             | Python, NumPy                                     |  
| **Alternatives**        | Replace `face_recognition` with DeepFace/InsightFace |  

---

## 🤝 Contributing  
1. Fork the repository.  
2. Create a branch: `git checkout -b feature/your-feature`.  
3. Test changes thoroughly.  
4. Submit a PR with a detailed description.  

---

## 📄 License  
MIT License. See [LICENSE](LICENSE).  

---

## 🙏 Acknowledgements  
- [Face Recognition Library](https://github.com/ageitgey/face_recognition) by Adam Geitgey.  
- Supabase for scalable database infrastructure.  
