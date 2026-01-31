

# 🚗 CarZone – Used Car Marketplace (Django)

CarZone is a **full-stack Django web application** built to simulate a **real used-car business platform**.
Users can browse cars, search based on their needs, create accounts, and send inquiries directly to the seller.
Admins can manage everything from a single dashboard.

This project is **live, deployed, and fully functional**.

---

## 🌐 Live Demo

🔗 [https://peaceful-atoll-32314-a8ed42453dba.herokuapp.com/](https://peaceful-atoll-32314-a8ed42453dba.herokuapp.com/)

---

## ✨ Features

### 👤 User Features

* User registration and login
* Google authentication (social login)
* Browse featured and latest cars
* Search and filter cars by:

  * Price
  * Model
  * Year
  * Location
  * Body type
* View detailed car information
* Send **car-specific inquiries**
* Send general messages through **Contact Us**
* Receive confirmation via backend processing

---

### 📩 Inquiry & Contact System

* Car inquiries are submitted directly from car detail pages
* Contact form allows general user questions
* All inquiries:

  * Are saved in the database
  * Trigger **real email notifications** to the admin

---

### 🛠 Admin Dashboard

* Secure admin login
* Add, update, and manage car listings
* Mark cars as featured
* View and manage customer inquiries
* Manage users and teams
* Manage social login configuration
* Manage deployed site settings

---

## 🧱 Project Structure

```text
carzone-project/
│
├── carzone/        # Main project settings and configuration
├── cars/           # Car listings, filters, and detail pages
├── contacts/       # Contact and inquiry handling
├── accounts/       # Authentication and social login
├── pages/          # Static pages (Home, About, Services, Contact)
├── templates/      # HTML templates
├── static/         # CSS, JavaScript, images
├── staticfiles/    # Collected static files for production
├── media/          # Uploaded car images
├── requirements.txt
├── Procfile
└── runtime.txt
```

This modular structure follows **real production-level Django architecture**.

---

## 🧑‍💻 Tech Stack

* **Backend:** Python, Django
* **Frontend:** HTML, CSS, Bootstrap
* **Database:** PostgreSQL
* **Authentication:** Django Auth, Google OAuth (Social Auth)
* **Email:** SMTP email notifications
* **Deployment:** Heroku, Gunicorn, WhiteNoise
* **Version Control:** Git, GitHub

---

## 🚀 Deployment

* Application is deployed on **Heroku**
* Static files handled using **WhiteNoise**
* Production server using **Gunicorn**
* Environment variables used for sensitive configuration

---

## 🎯 Why This Project?

This project was built to understand how **real backend systems work**, including:

* User authentication
* Data persistence
* Email workflows
* Admin dashboards
* Deployment to production

It is **not a tutorial-only project**, but a working application designed around real business use cases.

---

## 📌 Future Improvements

* Payment integration
* Role-based access control
* Analytics dashboard
* Improved UI/UX
* REST API support

---

## 📬 Contact

**Venkatesh**
📧 Email: [venkateshreddyningam@gmail.com](mailto:venkateshreddyningam@gmail.com)
💼 LinkedIn: [https://linkedin.com/in/venkateshreddyningam](https://linkedin.com/in/venkateshreddyningam)

---

⭐ If you find this project interesting, feel free to star the repository or reach out!

