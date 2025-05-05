# SimGear Market

SimGear Market is a full-stack e-commerce web application designed for sim racing enthusiasts. The platform allows users to browse and purchase sim racing gear such as wheels, pedals, gloves, and accessories. Built with modern technologies and optimized for performance, this project serves as both a real-world software engineering case study and a portfolio piece.

## Tech Stack

| Layer        | Technology                       |
|--------------|----------------------------------|
| Frontend     | React + Vite + TailwindCSS       |
| Backend      | FastAPI (Python)                 |
| Database     | PostgreSQL                       |
| ORM          | SQLAlchemy + Alembic             |
| Auth         | JWT (OAuth2PasswordBearer)       |
| Payments     | Stripe Checkout API              |
| Deployment   | Netlify (frontend), Render or Railway (backend)

## Features (MVP)

### User Experience
- Secure registration and login (JWT-based)
- Product catalog with filtering and search
- Responsive product detail pages
- Shopping cart with live totals
- Stripe-powered checkout
- Order confirmation and history

### Admin Tools
- Admin authentication
- Product management (CRUD)
- Order overview panel
