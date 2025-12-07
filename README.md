# Brother Call Reminder

A Django web application that sends email reminders when you forget to call your brother.

## Features
- Simple web interface
- Email notifications
- Beautiful responsive design

## Setup Instructions

1. Clone the repository:
```bash
   git clone https://github.com/YOUR_USERNAME/brother-call-reminder.git
   cd brother-call-reminder
```

2. Create virtual environment:
```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
   pip install -r requirements.txt
```

4. Configure email settings in `brother_reminder/settings.py`

5. Run migrations:
```bash
   python manage.py migrate
```

6. Run the server:
```bash
   python manage.py runserver
```

7. Visit http://127.0.0.1:8000/

## Technologies Used
- Python
- Django
- HTML/CSS/JavaScript