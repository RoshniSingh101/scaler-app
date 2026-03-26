# Scalable Video Processing Cluster

Distributed system designed to handle background tasks while scaling horizontally using Nginx, FastAPI, RabbitMQ, and Celery.



## The Architecture

* **Load Balancer:** Nginx (distributes traffic between app clones one and two)
* **Web Layer:** FastAPI (running replicated instances)
* **Task Broker:** RabbitMQ (asynchronously runs background jobs)
* **Background Worker:** Celery (processes video tasks).
* **Result Backend:** Redis (stores "True/False" results if async background tasks were successful and cache hit counters)
* **Caching Layer:** Memcached (High-speed volatile data storage).

---

## Features
* **Horizontal Scaling:** Nginx balances requests across `app-clone-1` and `app-clone-2`
* **Async Task Polling:** UI triggers a task, receives a `task_id`, and polls the server until the worker returns a result
* **Fault Tolerance:** Designed to stay online even if one app clone instance or the worker restarts
* **Real-time Feedback:** Displays which specific container handled the request via the `server_id`

---

## Getting Started

### Prerequisites
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.

### Installation & Launch
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/scaler-app.git]
    cd scaler-app
    ```

2.  **Spin up the entire cluster:**
    ```bash
    docker-compose up --build
    ```

3.  **Open the App:**
    Navigate to [http://localhost:8080](http://localhost:8080) in your browser.

---

## API Reference

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Renders the Dashboard with Hit Counter and Server ID |
| `POST` | `/process-video` | Submits a task to RabbitMQ. Returns a `task_id` |
| `GET` | `/task-status/{id}`| Checks Redis to see if the worker finished the job |

---

## Scaling the System
To see Nginx in action, you can scale your application clones dynamically:
```bash
# Scale to 5 instances of the first app clone
docker-compose up --scale app-clone-1=5 -d
```
---

## After Spinning Up the Cluster
You may tear it down and then spin it back up if you would like to make any changes on your local machine
```bash
docker-compose down
```
---
