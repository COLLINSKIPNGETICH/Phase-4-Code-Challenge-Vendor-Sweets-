# Phase-4-Code-Challenge-Vendor-Sweets-

This project is a Flask-based RESTful API for managing vendor sweets.

## Table of Contents

- [Overview](#overview)
- [Setup Instructions](#setup-instructions)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Testing](#testing)
- [License](#license)

## Overview

The Vendor Sweets API allows users to perform CRUD operations on vendor sweets, manage orders, and authenticate users.

The API follows RESTful principles and provides endpoints for managing users, sweets, and orders.

## Setup Instructions

Follow these steps to set up and run the Vendor Sweets API locally:

1. Clone the repository:

2. Navigate to the project directory:

3. Create and activate a virtual environment:

4. Install dependencies:

5. Set up the database:

6. Run the development server:

7. Access the API at `http://localhost:5000`.

## API Endpoints

### Users

- `POST /users`: Create a new user.
- `GET /users/<user_id>`: Get user details.
- `PUT /users/<user_id>`: Update user details.
- `DELETE /users/<user_id>`: Delete a user.

### Sweets

- `POST /sweets`: Create a new sweet.
- `GET /sweets/<sweet_id>`: Get sweet details.
- `PUT /sweets/<sweet_id>`: Update sweet details.
- `DELETE /sweets/<sweet_id>`: Delete a sweet.
- `GET /sweets`: Get a list of all sweets.

### Orders

- `POST /orders`: Place a new order.
- `GET /orders/<order_id>`: Get order details.
- `PUT /orders/<order_id>`: Update order details.
- `DELETE /orders/<order_id>`: Cancel an order.
- `GET /orders`: Get a list of all orders.

## Authentication

Authentication is required for certain endpoints. To authenticate, include an `Authorization` header with a valid JWT token:

## Testing

Run the test suite:

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.