from sqlalchemy import Column, Integer, String, Text
from app.database import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    github_url = Column(String)
    live_url = Column(String)
    tech_stack = Column(String)  # comma-separated or JSON
