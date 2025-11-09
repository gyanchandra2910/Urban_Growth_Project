"""Data loading utilities for Road Safety project"""
import pandas as pd
import os

def load_db():
    """Load the road safety database with automatic encoding detection"""
    csv_path = os.path.join(os.path.dirname(__file__), 'GPT_Input_DB.csv')
    
    encodings = ['utf-8', 'latin-1', 'iso-8859-1', 'cp1252']
    
    for encoding in encodings:
        try:
            df = pd.read_csv(csv_path, encoding=encoding)
            return df
        except (UnicodeDecodeError, Exception):
            continue
    
    raise ValueError(f"Could not load {csv_path} with any supported encoding")
