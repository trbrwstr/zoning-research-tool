#!/usr/bin/env python3
"""
Database initialization script.
Run this script to create all database tables.
"""

from app.models.database import engine, Base
from app.models.models import User, ZoningLookup, Subscription


def init_db():
    """Initialize the database with all tables."""
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")


if __name__ == "__main__":
    init_db()
