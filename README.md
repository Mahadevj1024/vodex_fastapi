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
```

### 2. Running locally
```bash
uvicorn app.main:app --reload
```

## Endpoints

### Items API
#### 1. **Create Item** - POST /items:
Input: Name, Email, Item Name, Quantity, Expiry Date.
Automatically adds Insert Date

#### 2. **Get Item by ID** - GET /items/{id}

#### 3. **Filter Items** - GET /items/filter:
Filter by Email, Expiry Date, Insert Date, Quantity.

#### 4. **Update Item** - PUT /items/{id}

#### 5. **Delete Item** - DELETE /items/{id}

#### 6. **MongoDB Aggregation** - GET /items/aggregate:
Aggregate items by email and return the count for each.

### User Clock-In Records API
#### 1. **Create clock-in** - POST /clock-in:
Input: Email, Location.
Automatically adds Insert DateTime

#### 2. **Get clock-in by ID** - GET /clock-in/{id}

#### 3. **Filter clock-in** - GET /clock-in/filter:
Filter by Email, Location, Insert DateTime.

#### 4. **Update clock-in** - PUT /clock-in/{id}

#### 5. **Delete clock-in** - DELETE /clock-in/{id}



