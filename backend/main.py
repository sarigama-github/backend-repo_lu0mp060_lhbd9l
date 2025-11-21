from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from schemas import QuoteRequest, ContactMessage
from database import create_document, db

app = FastAPI(title="TGAgout API", version="1.0.0")

# CORS for frontend dev server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"status": "ok", "service": "tgagout-backend"}


@app.get("/test")
def test_db():
    if db is None:
        raise HTTPException(status_code=500, detail="Database not available")
    try:
        # quick ping by listing collections
        collections = db.list_collection_names()
        return {
            "backend": "ok",
            "database": "ok",
            "database_url": "configured",
            "database_name": db.name,
            "connection_status": "connected",
            "collections": collections,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/quote")
def create_quote(payload: QuoteRequest):
    try:
        quote_id = create_document("quote", payload)
        return {"ok": True, "id": quote_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/contact")
def create_contact(payload: ContactMessage):
    try:
        msg_id = create_document("contactmessage", payload)
        return {"ok": True, "id": msg_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
