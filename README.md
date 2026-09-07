# 🌊 WaveChat

A real-time chat application built with Django and WebSockets. Multiple users can join rooms and chat instantly without any page refresh.

## ✨ Features
- Real-time messaging with WebSockets
- Multiple chat rooms
- User authentication (register, login, logout)
- Message history saved to database
- Typing indicators
- Online status
- Discord-inspired dark UI

## 🛠️ Tech Stack
- **Backend:** Python, Django, Django Channels
- **Real-time:** WebSockets, ASGI
- **Server:** Daphne
- **Database:** SQLite (dev) / PostgreSQL (prod)
- **Frontend:** HTML, CSS, JavaScript

## ⚙️ Run Locally

1. Clone the repo
```bash
   git clone https://github.com/yawasante-dev/wavechat.git
   cd wavechat
```

2. Create and activate virtual environment
```bash
   python -m venv venv
   venv\Scripts\activate
```

3. Install dependencies
```bash
   pip install -r requirements.txt
```

4. Run migrations
```bash
   python manage.py migrate
```

5. Create some rooms
```bash
   python manage.py shell
   from chat.models import Room
   Room.objects.create(name='general', slug='general', description='General chat')
   exit()
```

6. Start the server
```bash
   daphne -p 8000 wavechat.asgi:application
```

7. Visit `http://127.0.0.1:8000`

## 👤 Author
Asante — [GitHub](https://github.com/yawasante-dev)