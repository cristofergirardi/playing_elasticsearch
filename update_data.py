from database import client

es = client.get_es_client()


def update_rows():
    documents = [
      { "index": { "_index": "employees", "_id": "Qxyg3o4BjNxUpfJLfB7b"}},
      {"address": "Anywhere and somewhere Street"},
      { "index": { "_index": "employees", "_id": "Ihyg3o4BjNxUpfJLfB7b"}},
      {"name": "Anywhere and somewhere Street"}
    ]

    es.bulk(operations=documents)


if __name__ == '__main__': 
    update_rows()