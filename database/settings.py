def get_settings():
    settings = {
        "number_of_shards": 5,
        "number_of_replicas": 1,
        "analysis": {
            "analyzer": {
                "custom_analyzer": {
                    "tokenizer": "standard",
                    "filter" : ["fingerprint"], # Remove duplicates words
                    "stopwords": "_english_" # Remove prepositions
                    }
                }
            }
    }

    return settings