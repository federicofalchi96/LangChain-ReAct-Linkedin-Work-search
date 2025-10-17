from typing import List
from pydantic import BaseModel, Field

class Source(BaseModel):
    url: str = Field(description="LinkedIn URL dell'annuncio")
    title: str = Field(description="Titolo del lavoro o posizione", default="")
    location: str = Field(description="Località o tipo di lavoro (es. remoto, ibrido, Milano...)", default="")
    company: str = Field(description="Nome dell'azienda", default="")

class AgentResponse(BaseModel):
    answer: str = Field(description="Sintesi generale del risultato")
    sources: List[Source] = Field(default_factory=list, description="Lista delle offerte di lavoro trovate")
