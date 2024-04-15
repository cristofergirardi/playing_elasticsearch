# Description: This file contains the mapping for the Elasticsearch index.
def map_employees():
    mappings = {
        "properties": {
            "name": {"type": "text", "analyzer": "standard"},
            "age": {"type": "integer"},
            "email": {"type": "text", "analyzer": "standard"},
            "address": {"type": "text", "analyzer": "standard"},
            "phone": {"type": "text", "analyzer": "standard"},
            "phrase":{"type": "text", "analyzer": "custom_analyzer"},
            "company_name": {"type": "keyword", "analyzer": "standard"}
        }
    }

    return mappings

def map_companies():
    mappings = {
        "properties": {
            "name": {"type": "text", "analyzer": "standard"}
        }
    }

    return mappings
