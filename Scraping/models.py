from mongoengine import connect, Document, StringField, ListField
import certifi

connect(db="HW_Web_9",
        host=f"mongodb+srv://web_dz08:15061992@artem.z75si5r.mongodb.net/?retryWrites=true&w=majority",
        tlsCAFile=certifi.where())


class Quote(Document):
    author = StringField(required=True)
    quote = StringField()
    tags = ListField(StringField())
    meta = {"collection": "Quote"}


class Author(Document):
    fullname = StringField()
    born_date = StringField()
    born_location = StringField()
    description = StringField()
    meta = {"collection": "Author"}
