# Attendance Management System

This is a web-based **Attendance Management System**, originally designed for community organizations, that allows registering, managing, and tracking attendance of members efficiently.

## 📌 Features

- Register users and members of the organization.
- Daily attendance management.
- Attendance reporting and visualization.
- User-friendly web interface accessible through any browser.
- Management of member-related media files.

## 🛠️ Technologies Used

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (default)
- **Other Libraries:** See `requirements.txt` for additional dependencies

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/SebastianZutrep/asistencia-casa-de-paz.git
   cd asistencia-casa-de-paz
   
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   
3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Create a fresh local database:
   ```bash
   python manage.py migrate

5. (Optional) Create a superuser to access the Django admin panel:
   ```bash
   python manage.py createsuperuser

6. Run the local server:
   ```bash
   python manage.py runserver
Access http://127.0.0.1:8000 in your browser.

## Project Structure

Asistencia_Casa_De_Paz/
         casa_paz/
         │
         ├── casa_paz/       # Main application
         ├── asistencia/     # Attendance management functionalities
         ├── staticfiles/    # Static files (CSS, JS, images)
         ├── media/          # Member media files
         ├── db.sqlite3      # Database
         ├── manage.py
         └── requirements.txt

## 🤝 Contributing

To contribute safely to this project:

1. **Fork the repository** – this creates a personal copy of the project in your GitHub account.
2. **Create a branch** for your feature or bugfix:
   ```bash
   git checkout -b feature/new-feature

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for more details.


