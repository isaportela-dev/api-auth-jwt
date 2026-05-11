import sys
import os

os.environ["DATABASE_URL"] = "postgresql://postgres:postgres@localhost:5432/auth_db"

sys.path.insert(0, os.path.abspath("."))