"""
TF-IDF Search Module for Road Safety Database
Implements efficient search with in-memory caching of vectorizer and matrix
"""

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from load_data import load_db

# Global cache for vectorizer and TF-IDF matrix
_vectorizer = None
_tfidf_matrix = None
_dataframe = None

def _initialize_search():
    """
    Initialize the search system by loading data and creating TF-IDF matrix.
    This is called automatically on first search and cached for subsequent searches.
    """
    global _vectorizer, _tfidf_matrix, _dataframe
    
    if _vectorizer is not None and _tfidf_matrix is not None and _dataframe is not None:
        return  # Already initialized
    
    print("Initializing TF-IDF search system...")
    
    # Load the database
    _dataframe = load_db()
    
    # Create combined text column from specified fields
    text_columns = ['problem', 'type', 'category', 'data']
    
    # Handle missing values and combine columns
    _dataframe['combined_text'] = _dataframe[text_columns].fillna('').agg(' '.join, axis=1)
    
    # Create and fit TF-IDF vectorizer
    _vectorizer = TfidfVectorizer(
        max_features=1000,
        stop_words='english',
        ngram_range=(1, 2),  # Use unigrams and bigrams
        min_df=1,
        max_df=0.95
    )
    
    # Fit and transform the documents
    _tfidf_matrix = _vectorizer.fit_transform(_dataframe['combined_text'])
    
    print(f"✓ TF-IDF system initialized:")
    print(f"  - Documents: {_tfidf_matrix.shape[0]}")
    print(f"  - Features: {_tfidf_matrix.shape[1]}")
    print(f"  - Vocabulary size: {len(_vectorizer.vocabulary_)}")

def tfidf_search(query, top_n=5):
    """
    Search the database using TF-IDF and cosine similarity.
    
    Args:
        query (str): Search query text
        top_n (int): Number of top results to return (default: 5)
    
    Returns:
        list of dict: Top N results with fields:
            - id: Row index
            - score: Cosine similarity score (0-1)
            - problem: Problem description
            - data: Detailed data
            - clause: IRC clause reference
    """
    # Initialize search system if not already done
    _initialize_search()
    
    if not query or not query.strip():
        return []
    
    # Transform the query using the fitted vectorizer
    query_vec = _vectorizer.transform([query])
    
    # Calculate cosine similarity between query and all documents
    similarities = cosine_similarity(query_vec, _tfidf_matrix).flatten()
    
    # Get top N indices sorted by similarity (descending)
    top_indices = similarities.argsort()[-top_n:][::-1]
    
    # Prepare results
    results = []
    for idx in top_indices:
        score = similarities[idx]
        
        # Only include results with non-zero similarity
        if score > 0:
            row = _dataframe.iloc[idx]
            results.append({
                'id': int(idx),
                'score': float(score),
                'problem': str(row['problem']),
                'data': str(row['data']),
                'clause': str(row['clause'])
            })
    
    return results

def reset_cache():
    """
    Reset the cached vectorizer and TF-IDF matrix.
    Useful if the database is updated.
    """
    global _vectorizer, _tfidf_matrix, _dataframe
    _vectorizer = None
    _tfidf_matrix = None
    _dataframe = None
    print("✓ Search cache reset")

def get_cache_info():
    """
    Get information about the current cache state.
    
    Returns:
        dict: Cache information including initialization status and sizes
    """
    return {
        'initialized': _vectorizer is not None,
        'num_documents': _tfidf_matrix.shape[0] if _tfidf_matrix is not None else 0,
        'num_features': _tfidf_matrix.shape[1] if _tfidf_matrix is not None else 0,
        'vocabulary_size': len(_vectorizer.vocabulary_) if _vectorizer is not None else 0
    }

if __name__ == '__main__':
    # Test the search functionality
    print("="*80)
    print("TF-IDF SEARCH TEST")
    print("="*80)
    
    # Test queries
    test_queries = [
        "damaged signs",
        "height issue",
        "missing",
        "placement problem",
        "faded"
    ]
    
    for query in test_queries:
        print(f"\n🔍 Query: '{query}'")
        print("-" * 80)
        
        results = tfidf_search(query, top_n=3)
        
        if results:
            for i, result in enumerate(results, 1):
                print(f"\n{i}. Score: {result['score']:.4f} | ID: {result['id']}")
                print(f"   Problem: {result['problem']}")
                print(f"   Clause: {result['clause']}")
                print(f"   Data: {result['data'][:100]}...")
        else:
            print("   No results found")
    
    print("\n" + "="*80)
    print("CACHE INFORMATION")
    print("="*80)
    cache_info = get_cache_info()
    for key, value in cache_info.items():
        print(f"{key}: {value}")
