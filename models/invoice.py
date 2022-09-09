from .base import BaseModel
from fields import BaseField


class Invoice(BaseModel):

    _id = BaseField("Id")
    date = BaseField("TxnDate")
    sync_token = BaseField("SyncToken")
    doc_number = BaseField("DocNumber")

    def __init__(self, id, date, sync_token, doc_number):
        self._id = id
        self.date = date
        self.sync_token = sync_token
        self.doc_number = doc_number

    @property
    def id(self):
        return self._id