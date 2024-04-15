from database import client

es = client.get_es_client()

def select_one_row():
    query = {
        "size": 1, # Get one row
        "query": {
            "bool": {
                "must": {
                    "match": {
                        "age": 53,
                    }
                }
            }
        }
    }

    resp = es.search(index="employees", body=query)
    print(resp)

def select_count_row():
    query = {
        "query": {
            "bool": {
                "must": {
                    "match": {
                        "age": 53,
                    }
                }
            }
        }
    }

    resp = es.search(index="employees", body=query)
    print(f'Found {len(resp["hits"]["hits"])} rows.')
    for row in resp["hits"]["hits"]:
        print(row["_source"]["name"])


if __name__ == '__main__':
    # select_one_row()    
    select_count_row()