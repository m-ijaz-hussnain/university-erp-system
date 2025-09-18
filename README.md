
# 🎓 University ERP System

A **modular University ERP system** built with **Django** and **Django REST Framework** to streamline institutional operations.
Manages students, faculty, academics, administration, library, and financial workflows efficiently.
Offers **secure**, **scalable** RESTful APIs for seamless integration with external systems or frontends.

---

## 🚀 Key Modules


### 🛠️ Administration

* User & Role Management (Admins, Faculty, Staff, Students)
* Department & Batch Management
* Course Management

### 👨‍🎓 Student Management

* Student Registration & Profile Handling
* Attendance Tracking
* Academic Performance (Grades, Exams)

### 👩‍🏫 Faculty Management

* Faculty Profile Management
* Course Assignments
* Attendance & Grade Submission

### 📚 Academic Operations

* Course Scheduling
* Exam Management
* Grade Calculation & Reports

### 📖 Library Management

* Book Inventory & Categorization
* Book Lending & Returns
* Fine Calculation

### 💰 Financial Accounting

* Fee Collection & Tracking
* Scholarship Management
* Invoice Generation

### 📊 Reporting & Analytics

* Student Performance Reports
* Faculty Reports
* Financial & Academic Summaries

---

## 🧰 Tech Stack

| Technology                | Description                       |
| ------------------------- | --------------------------------- |
| **Django**                | Backend Web Framework             |
| **Django REST Framework** | RESTful API Development           |
| **PostgreSQL / SQLite**   | Relational Database               |
| **JWT Authentication**    | Secure Token-Based Authentication |
| **Docker (Optional)**     | Containerization & Deployment     |
| **Bootstrap / Tailwind**  | UI Styling (if applicable)        |

---

## 📡 API Overview

All modules are accessible via **RESTful APIs** with **JWT-based authentication**.

| Module   | Base Endpoint    |
| -------- | ---------------- |
| Auth     | `/api/auth/`     |
| Students | `/api/students/` |
| Faculty  | `/api/faculty/`  |
| Courses  | `/api/courses/`  |
| Exams    | `/api/exams/`    |
| Library  | `/api/library/`  |
| Finance  | `/api/finance/`  |
| Reports  | `/api/reports/`  |

📄 *Full API documentation coming soon in* `docs/api_overview.md`

---

## ⚙️ Installation

Follow these steps to set up the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/university-erp-system.git
cd university-erp-system
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root and set the following (example):

```env
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///db.sqlite3
```

### 5. Apply Migrations

```bash
python manage.py migrate
```

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

---

## 🐳 Docker Setup (Optional)

To run the project with Docker:

```bash
docker-compose up --build
```

---

## ✅ Contributing

Contributions are welcome!
Please fork the repository and submit a pull request for any improvements or fixes.

---

## 📄 License

This project is licensed under the MIT License.

---

## 📬 Contact

For any queries or collaboration ideas, feel free to reach out at:
📧 **[mijazhussnain83@gmail.com](mailto:mijazhussnain83@gmail.com)**
🌐 [GitHub Profile](https://github.com/m-ijaz-hussnain)

---

