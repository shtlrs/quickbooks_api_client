from .base import BaseModel
from fields import BaseField


class Invoice(BaseModel):

    _id = BaseField("Id")
    date = BaseField("TxnDate")
    sync_token = BaseField("SyncToken")
    doc_number = BaseField("DocNumber")
    table_name = "Invoice"

    def __init__(self, id, date, sync_token, doc_number):
        self._id = id
        self.date = date
        self.sync_token = sync_token
        self.doc_number = doc_number

    def from_dict(self, json) -> BaseModel:
        return Invoice(
            id=json.get(Invoice._id),
            doc_number=json.get(Invoice.doc_number),
            sync_token=json.get(Invoice.sync_token),
            date=json.get(Invoice.date)
        )

    @property
    def id(self):
        return self._id
