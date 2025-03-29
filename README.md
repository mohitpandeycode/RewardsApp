# Rewards App Project README

## Project Description

Rewards Help is a Django-based web application designed to manage and track user rewards based on their interactions with various applications. It provides functionalities for users to earn rewards by downloading and using specified apps, and for administrators to validate and manage these rewards. This project focuses on providing a streamlined system for reward distribution and tracking.

## Features

**User-Facing Features:**

* **User Registration and Login:**
    * Secure user registration and authentication using Django's built-in system.
* **App Discovery:**
    * Users can browse a list of available applications.
    * Detailed app information including name, category, subcategory, image, and points.
* **App Download Tracking:**
    * Users can mark apps as downloaded.
    * Download history is recorded with timestamps.
* **Screenshot Uploads:**
    * Users can upload screenshots as proof of app usage.
    * Screenshot uploads are associated with specific app downloads.
* **Reward Points Display:**
    * Users can see the reward points associated with each app.
* **OTP Verification:**
    * Users are able to be sent an OTP for account verification.

**Administrator-Facing Features:**

* **Admin Dashboard:**
    * Access to an administrative dashboard for managing user rewards.
    * Admin can add , Update and delete the apps for rewards.
* **Screenshot Validation:**
    * Administrators can view user-uploaded screenshots.
    * Administrators can validate or invalidate screenshots.
* **Reward Invalidation:**
    * Administrators can invalidate app rewards if the proof is not valid.
    * Invalidated rewards are removed from user accounts.
* **User Download History:**
    * Administrators can view the download history of individual users.
    * Administrators can see all users downloaded apps.
* **User Information Display:**
    * Administrators can view all user information.

## Technologies Used

* **Django:** Python web framework for backend development.
* **Python:** Programming language.
* **HTML/CSS/JavaScript:** Frontend development.
* **Git/GitLab:** Version control and repository management.
* **Database:**  SQLite
* **Django Messages:** For user feedback.
* **Django Authentication:** For user authentication.
* **Twillo:** For OTP authentication.
* **ImageField:** For handling image uploads.

## GitLab Setup

This project is hosted on GitLab. To clone and run this project:

1.  **Clone the Repository:**

    ```bash
    git clone https://gitlab.com/mohitpandeycode/rewardsapp
    cd RewardsApp
    ```

2.  **Create a Virtual Environment (Recommended):**

    ```bash
    python -m virtualenv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows
    ```

3.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Database:**

    * Modify the `DATABASES` setting in `rewards-help/settings.py` to match your database configuration.
    * Run migrations.

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Create Superuser(Admin):**

    ```bash
    python manage.py createsuperuser
    ```

6.  **Run Development Server:**

    ```bash
    python manage.py runserver
    ```

7.  **Access the Application:**

    * Open your web browser and navigate to `url`.

# Demo video of the Application:
 1. **URL of the Demo video:**

    * `url`.


# Problem Set 3

## A. Write and share a small note about your choice of system to schedule periodic tasks (such as downloading a list of ISINs every 24 hours). Why did you choose it? Is it reliable enough; Or will it scale? If not, what are the problems with it? And, what else would you recommend to fix this problem at scale in production?

## Answer:
For scheduling periodic tasks like downloading a list of ISINs every 24 hours, I would choose Celery with Django and Celery Beat.
### Why Celery?
Celery is a powerful, distributed task queue that integrates well with Django. Combined with Celery Beat, it allows us to schedule tasks at specific intervals, making it perfect for our use case.

### Reliability & Scalability
Celery is quite reliable for periodic tasks, but its scalability depends on the broker and backend configuration. Using Redis or RabbitMQ as the message broker ensures fast task execution, while a database or Redis as the result backend helps manage task states. However, as the workload increases, Celery workers need to be scaled accordingly to handle more tasks efficiently.

### Potential Problems
* Single Worker Bottleneck: If running with only one worker, tasks may get delayed or stuck if there's a backlog.

* Database Overhead: If the result backend is a database, it may slow down over time due to excessive writes.

* Task Failures & Retries: If a task fails, retries need to be handled properly to avoid data inconsistency.

### Production-Scale Recommendations
For a more scalable production setup:

* Use a Dedicated Message Broker: Redis (fast and lightweight) or RabbitMQ (better for complex workflows).

* Run Multiple Celery Workers: Helps distribute the load across multiple processes.

* Use Celery with Kubernetes: For auto-scaling workers based on load.

* Monitor Tasks: Use Flower or Prometheus + Grafana to track task execution and failures.


## B. In what circumstances would you use Flask instead of Django and vice versa?
## Answer:
### When to Use Flask Instead of Django:
### Flask is a lightweight, micro-framework, making it ideal for:

* Small or Simple Projects – If you need a quick REST API, prototype, or microservice, Flask’s minimal setup is a great advantage.

* High Customization Needs – Flask gives you more flexibility to choose components like authentication, database ORM, and templating.

* Microservices Architecture – Since Flask is lightweight, it's often used in a microservices setup where each service handles a specific function.

* Low Overhead Performance – Flask has less overhead compared to Django, making it slightly faster for simple API requests.

* Learning Purposes – If you're new to web frameworks and want to understand the internals of web development, Flask is great for learning.

### When to Use Django Instead of Flask
### Django is a full-stack framework, best suited for:

* Large or Complex Applications – If you need an admin panel, authentication, ORM, and templating, Django provides everything out of the box.

* Rapid Development – With Django’s built-in features, you can build a production-ready web app quickly.

* Security & Scalability – Django includes security features (CSRF protection, authentication) and supports horizontal scaling.

* Data-Driven Applications – If your app requires a lot of database operations, Django’s ORM simplifies database interactions.

* Team Collaboration – Django enforces a structured project layout, making it easier for teams to work together.


