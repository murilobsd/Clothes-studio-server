from base.models import BaseModel
from schematics.types import IntType, StringType
from schematics.types.compound import ListType
from schematics.exceptions import ValidationError, ModelConversionError


class ItemModel(BaseModel):
    MONGO_COLLECTION = 'items'
    name = StringType(required=True)
    images = ListType(StringType, required=True)
    tags = ListType(StringType())
    cost = IntType(default=0)
    category = StringType(required=True)


if __name__ == "__main__":
    item = ItemModel(
        {
            'name':     '',
            'images':   '12.jpg, 11.jpg',
            'tags':     [],
            # 'cost':     12,
            'category': "dresses"
        }
    )

    try:
        item.validate()
        print(item.to_primitive())
    except ValidationError as e:
        print(e.messages)