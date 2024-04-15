from database import client, mappings, settings
from common.read_file import JsonRead
from elasticsearch import BadRequestError, helpers

def get_data():

    es = client.get_es_client()
    # Creating inverted indexes and setups
    try:
        resp_employees = es.indices.create(index="employees", mappings=mappings.map_employees(), settings=settings.get_settings())
        print(resp_employees)
    except BadRequestError as e:
        print("Employees' index has already been created.")

    try:
        resp_companies = es.indices.create(index="companies", mappings=mappings.map_companies())
        print(resp_companies)
    except BadRequestError as e:
        print("Companies' index has already been created.")        
    
    file = JsonRead()
    print("Reading file...")
    file.read_file()

    # Using bulk to add our data    
    print("Adding employees...")
    for chunk in file.get_employees():
        bulk_data = []
        for i, row in chunk.iterrows():
            bulk_data.append(
                {
                    "_index": "employees",
                    # "_id": i, # ElasticSearch manage it
                    "_source": {
                        "name": row["name"],
                        "email" : row["email"],
                        "address" : row["address"],
                        "age" : row["age"],
                        "phone" : row["phone"],
                        "phrase" : row["phrase"],
                        "company_name" : row["company_name"]
                    } 
                }
            )
        helpers.bulk(es, bulk_data)

    print("Adding companies...")   
    bulk_data = []
    for row in file.get_companies():
        bulk_data.append(
            {
                "_index": "companies",
                # "_id": i, # ElasticSearch manage it
                "_source": {
                    "name": row
                } 
            }
        )
    helpers.bulk(es, bulk_data)

    # Validate my insert of data
    # es.indices.refresh(index="employees")
    # es.cat.count(index="employees", format="json")
    print(f'Total employees = {es.count(index="employees")}')
    print(f'Total companies = {es.count(index="companies")}')


if __name__ == '__main__':
    get_data()
