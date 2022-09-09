
# Description

The purpose of this project is to have a minimalistic way to construct basic queries that will be later used to fetch
data from quickbooks and provides a basic API wrapper over their web APIs.

> Note: 
> 
> * This project offers implementation to only a couple of resources
> * This project only offers the following:
>   * Fetch a resource by id
>   * Search for a resource based on a particular query
>   * Delete a resource
> * This project currently has a very simple implementation of the Invoice model only

#  Quickstart

First thing you'll need to do is to set the `ACCESS_TOKEN` environment variable.

## Fetch a particular invoice

```py

from client import QuickBooksApiClient
from config import ACCESS_TOKEN
from enums import Resource

client = QuickBooksApiClient(access_token=ACCESS_TOKEN)
invoice_id = 12345

invoice_data = client.get(resource_id=invoice_id, resource=Resource.INVOICE)

```

## Search for a particular invoice 

```py

from client import QuickBooksApiClient
from config import ACCESS_TOKEN
from models import Invoice
from builder import Query
from builder.conditions import Equals

invoice_name = "Business dinner"
query = Query().SELECT(Invoice.ALL).FROM(Invoice.table_name).WHERE(Equals(Invoice.doc_number, invoice_name))
client = QuickBooksApiClient(access_token=ACCESS_TOKEN)

invoice_data = client.query(query=query)
invoice = Invoice.from_dict(invoice_data)
```


## Areas of improvement
> * Add multiple field types with custom validation predicates
> * Add serialization classes (Maybe even use Django Rest Framework's ?)
> * Add support for nested fields