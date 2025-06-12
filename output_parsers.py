from typing import List, Dict, Any
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


class Summary(BaseModel):
    summary: str = Field(description="summary")
    facts: List[str] = Field(description="interesting facts about them")

    def to_dict(self) -> Dict[str, Any]:
        return {"summary": self.summary, "facts": self.facts}


class Email(BaseModel):
    subject: str = Field(description="email subject line")
    body: str = Field(description="email body content")

    def to_dict(self) -> Dict[str, Any]:
        return {"subject": self.subject, "body": self.body}


summary_parser = PydanticOutputParser(pydantic_object=Summary)
email_parser = PydanticOutputParser(pydantic_object=Email)
