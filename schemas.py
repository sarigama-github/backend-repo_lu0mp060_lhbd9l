from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# Following the convention: class name lowercased -> collection name

class QuoteRequest(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=120)
    empresa: Optional[str] = Field(default=None, max_length=160)
    telefono: Optional[str] = Field(default=None, max_length=40)
    email: EmailStr
    origen: str
    destino: str
    tipo_mercancia: Optional[str] = None
    peso_volumen: Optional[str] = None
    comentarios: Optional[str] = None

class ContactMessage(BaseModel):
    nombre: str
    email: EmailStr
    mensaje: str
