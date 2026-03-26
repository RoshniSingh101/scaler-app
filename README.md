# 🚀 Scalable Video Processing Cluster

A high-availability, distributed system designed to handle heavy background tasks using a Producer-Consumer architecture. This project demonstrates how to scale a web application horizontally using Nginx, FastAPI, RabbitMQ, and Celery.



## 🏗️ The Architecture
This stack is built to solve the "Slow Request" problem. Instead of making a user wait for a heavy task to finish, we offload the work to background workers.

* **Load Balancer:** Nginx (Distributes traffic between App Clones).
* **Web Layer:** FastAPI (Running multiple replicated instances).
* **Task Broker:** RabbitMQ (The "Post Office" for background jobs).
* **Background Worker:** Celery (The "Factory" that does the heavy lifting).
* **Result Backend:** Redis (Stores the "True/False" results and hit counters).
* **Caching Layer:** Memcached (High-speed volatile data storage).

---

## 🛠️ Features
* **Horizontal Scaling:** Nginx balances requests across `app-clone-1` and `app-clone-2`.
* **Async Task Polling:** The UI triggers a task, receives a `task_id`, and polls the server until the worker returns a result.
* **Fault Tolerance:** Designed to stay online even if one app instance or the worker restarts.
* **Real-time Feedback:** The "Fancy UI" displays which specific container handled the request via the `server_id`.

---

## 🚦 Getting Started

### Prerequisites
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.

### Installation & Launch
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/scaler-app.git](https://github.com/your-username/scaler-app.git)
    cd scaler-app
    ```

2.  **Spin up the entire cluster:**
    ```bash
    docker-compose up --build
    ```

3.  **Open the App:**
    Navigate to [http://localhost:8080](http://localhost:8080) in your browser.

---

## 🚦 API Reference

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Renders the Dashboard with Hit Counter and Server ID. |
| `POST` | `/process-video` | Submits a task to RabbitMQ. Returns a `task_id`. |
| `GET` | `/task-status/{id}`| Checks Redis to see if the worker finished the job. |

---

## 📈 Scaling the System
To see Nginx in action, you can scale your application clones dynamically:
```bash
# Scale to 5 instances of the first app clone
docker-compose up --scale app-clone-1=5 -d