# 🔐 Django Custom Authentication System

> Simple & secure user authentication with custom user model, forms, and manual HTML login/register pages.

---

## 🚀 Features

- ✅ Custom User Model with extra fields  
- 📝 User Registration using Django's `UserCreationForm` subclass  
- 🔑 Secure Login with email or username support  
- 🎨 Manual HTML/CSS forms for login & registration  
- 🔄 Full workflow: forms → view → model → authentication → session

---

---

## 🔍 How It Works (User Login Flow)

1. 🧑‍💻 User opens login page and fills in credentials (username or email + password).  
2. 📡 Form sends POST request to Django login view.  
3. 🔄 View parses data, uses custom logic to map email to username if needed.  
4. 🔐 `authenticate()` checks user credentials against database with hashed passwords.  
5. ✅ On success, `login()` creates session to keep user authenticated.  
6. 🚪 Redirect to protected home/dashboard page.  
7. ❌ On failure, user sees “Invalid credentials” error and can retry.

---

## 💡 Tips & Notes

- ✔️ Use Django's `create_user()` for password hashing on registrations  
- ⚙️ Configure `AUTH_USER_MODEL` in settings.py for custom user model support  
- 🎨 Customize forms and templates for UX and branding  
- 🔒 Always include `{% csrf_token %}` in forms for security  
- 🐍 Leverage Django’s built-in authentication framework for reliability

---
