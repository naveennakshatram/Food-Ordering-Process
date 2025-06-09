# Food-Ordering-Process
Cloud-native food ordering system with microservices for Client, Hotel, and Delivery. Built using Python (FastAPI/Flask) and deployed on Kubernetes with internal service communication.


# 🍔 Cloud-Native Food Ordering System

This project implements a simple cloud-native microservices-based food ordering system using Python and Kubernetes. The application is split into three independent services—**Client**, **Hotel**, and **Delivery**—each running in its own pod and communicating via internal REST APIs.

## 🧱 Microservices Overview

* **Client Service**: Accepts food orders from users and initiates the order process.
* **Hotel Service**: Receives orders from the client, processes food preparation, and notifies the delivery service.
* **Delivery Service**: Handles food pickup and delivery to the user once the order is ready.

## ⚙️ Tech Stack

* **Language**: Python (FastAPI for Client & Delivery, Flask for Hotel)
* **Platform**: Kubernetes
* **Ingress**: NGINX Ingress Controller for exposing the Client service
* **Service Communication**: Internal DNS-based service discovery (e.g., `http://hotel-svc`, `http://delivery-svc`)

## 🚀 Deployment

Each service is containerized using Docker and deployed via Kubernetes manifests. Only the Client service is exposed externally through an Ingress resource.

## 📂 Folder Structure

```
.
├── client/
│   └── app.py
├── hotel/
│   └── app.py
├── delivery/
│   └── app.py
├── k8s/
│   ├── client-deployment.yaml
│   ├── hotel-deployment.yaml
│   ├── delivery-deployment.yaml
│   ├── ingress.yaml
│   └── services.yaml
├── README.md
└── requirements.txt
```

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

