# FastAPI CRUD Application

This FastAPI project performs CRUD operations for **Items** and **User Clock-In Records**. It includes features like filtering, MongoDB aggregation, and automatic API documentation using Swagger UI. 

## Features

- **CRUD Operations** for Items and Clock-In Records.
- **Filtering and Aggregation**: Filter items based on criteria like Email, Expiry Date, Quantity, etc., and use MongoDB aggregation to group item counts by email.
- **API Documentation**: Swagger UI for easy interaction with APIs.

## Installation

To run this project locally, follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/Mahadevj1024/vodex_fastapi.git
cd vodex_fastapi

### 2. Running locally
uvicorn app.main:app --reload
