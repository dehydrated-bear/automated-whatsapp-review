# Chat App Backend - FastAPI WhatsApp Review Collector

Backend API for collecting and managing customer reviews via WhatsApp integration.

## 📋 Quick Overview

- **Framework:** FastAPI
- **Database:** SQLAlchemy (SQLite/PostgreSQL)
- **Server:** Uvicorn
- **Language:** Python 3.8+
- **API Type:** REST API with WhatsApp webhook support

## 🚀 Quick Start

### 1. Setup Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Server

```bash
python main.py
```

Server will start at: `http://localhost:8000`

## 📁 File Structure

```
chat-app/
├── main.py                 # FastAPI application and endpoints
├── models.py              # SQLAlchemy database models
├── db.py                  # Database configuration
├── conversation.py        # WhatsApp message processing
├── requirements.txt       # Python dependencies
└── reviews.db            # SQLite database (created automatically)
```

## 🔌 API Endpoints

### Get All Reviews
```
GET /api/reviews
```
Returns array of all stored reviews.

### WhatsApp Webhook
```
POST /whatsapp/webhook
Content-Type: application/x-www-form-urlencoded

From=+1234567890&Body=Review+text
```
Receives and processes WhatsApp messages.

### Health Check
```
GET /
```
Returns server status.

## 📦 Dependencies

Key packages in `requirements.txt`:
- `fastapi` - Web framework
- `uvicorn` - ASGI server
- `sqlalchemy` - ORM
- `pydantic` - Data validation
- `python-dotenv` - Environment variables

## 🛠️ Configuration

### Environment Variables

Create `.env` file:
```env
DATABASE_URL=sqlite:///./reviews.db
FASTAPI_ENV=development
API_PORT=8000
```

### Database Setup

Database is automatically created on first run. To reset:
```bash
rm reviews.db
python main.py
```

## 🚢 Deployment

## hosted on render at 
 https://automated-whatsapp-review.onrender.com/  - server status
 https://automated-whatsapp-review.onrender.com/api/reviews - returns the list of all the reviews

## 🔐 CORS Configuration

CORS is enabled for all origins (development). For production, update:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-frontend.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## 📚 API Response Format

Reviews are returned in this format:
```json
{
  "id": 1,
  "user_name": "John Doe",
  "product_name": "Product Name",
  "product_review": "Great product!",
  "contact_number": "+1234567890",
  "created_at": "2025-11-20T16:31:05.063037+00:00"
}
```

## 🧪 Testing

### Test GET Endpoint
```bash
curl http://localhost:8000/api/reviews
```

### Test POST Endpoint
```bash
curl -X POST http://localhost:8000/whatsapp/webhook \
  -d "From=%2B1234567890&Body=Test+review"
```

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Find process using port 8000
lsof -ti:8000 | xargs kill -9  # macOS/Linux

# On Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

```



| **Last Updated:** November 20, 2025
