# Food-Ordering-Process
Cloud-native food ordering system with microservices for Client, Hotel, and Delivery. Built using Python (FastAPI/Flask) and deployed on Kubernetes with internal service communication.


# 🍔 Cloud-Native Food Ordering System

This project implements a simple cloud-native microservices-based food ordering system using Python and Kubernetes. The application is split into three independent services—**Client**, **Hotel**, and **Delivery**—each running in its own pod and communicating via internal REST APIs.

## 🧱 Microservices Overview

* **Client Service**: Accepts food orders from users and initiates the order process.
* **Hotel Service**: Receives orders from the client, processes food preparation, and notifies the delivery service.
* **Delivery Service**: Handles food pickup and delivery to the user once the order is ready.

| Service      | Role                                                                 |
| ------------ | -------------------------------------------------------------------- |
| **Client**   | Browses menu, places order, tracks delivery, and gives hotel ratings |
| **Hotel**    | Manages menus, accepts/declines orders, prepares food                |
| **Delivery** | Assigns delivery boys, tracks delivery status                        |

## 🧑‍🤝‍🧑 Entities:
2 Clients

2 Hotels (with individual menus)

2 Delivery Boys

## 🌐 Communication Flow
Client -> Hotel -> Delivery -> Client (Rating)

## 📦 Architecture
                       ┌────────────────────┐
                       │     Istio Ingress  │
                       │   (Gateway + VS)   │
                       └─────────┬──────────┘
                                 │
                ┌──────────────────────────────────────┐
                │                                      │
       ┌────────▼────────┐                   ┌────────▼────────┐
       │  client-svc     │───►Order────────►│   hotel-svc      │
       │  (FastAPI)      │◄──Track & Rate───│   (Flask)        │
       └──────┬──────────┘                   └────────┬────────┘
              │                                        │
              │                                        │
              ▼                                        ▼
     ┌─────────────┐                          ┌─────────────┐
     │ delivery-svc│◄──────Dispatch Order────▶│ Assign Rider│
     │  (FastAPI)  │                          └─────────────┘
     └─────────────┘
 




## ⚙️ Tech Stack

* **Language**: Python (FastAPI for Client & Delivery, Flask for Hotel)
* **Platform**: Kubernetes
* **Ingress**: NGINX Ingress Controller for exposing the Client service
* **Service Communication**: Internal DNS-based service discovery (e.g., `http://hotel-svc`, `http://delivery-svc`)

## 🚀 Deployment

Each service is containerized using Docker and deployed via Kubernetes manifests. Only the Client service is exposed externally through an Ingress resource.

## 📂 Folder Structure

![Folder Structure](Readme-images/FolderStructure.png)

## 📦 How to Run

```bash
# Apply Kubernetes resources
kubectl apply -f k8s/

# Access the app via Ingress
http://<your-domain-or-ip>/order
```

## 📬 Example API Flow

1. `POST /order` (Client) → calls Hotel service.
2. Hotel processes and calls Delivery.
3. Delivery service confirms the order is en route.


# ✅ Microservices Status

| Microservice | Port | Status |
| ------------ | ---- | ------ |
| Client       | 8001 | ✅ Done |
| Hotel        | 8002 | ✅ Done |
| Delivery     | 8003 | ✅ Done |


# ❌ Problem
     When you run 3 services in separate Docker containers locally (via docker run), 
     they do not share the same Docker network by default.

     That’s why when the Client service tries to reach  http://0.0.0.0:8001, it fails with:

     httpx.ConnectError: All connection attempts failed


# ✅ Solutions
## ✅ Option 1: Use a Docker user-defined bridge network

     This is the easiest and cleanest fix.

## 🔧 Step-by-Step Fix:
     1. Create a Docker network
          docker network create microservice-net

     2. Run each container in that network
          # Client:
               docker run -d --name client-service --network microservice-net -p 8000:8000 client
          # Hotel:
               docker run -d --name hotel-service --network microservice-net -p 5001:5001 hotel
          # Delivery:
               docker run -d --name delivery-service --network microservice-net -p 5002:5002 delivery

     3. Update service URLs in client/app/services.py
          Use container names as hostnames:
               HOTEL_SERVICE_URL = "http://hotel:5001"
               DELIVERY_SERVICE_URL = "http://delivery:5002"


## 🔍 View Logs from Docker Containers
     docker logs -f <container_name>

     Replace <container_name> with one of: client, hotel, or delivery.

     Example:
          docker logs -f client

          The -f flag means "follow" (like tail -f).
