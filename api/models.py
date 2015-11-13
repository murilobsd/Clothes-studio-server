from base.models import BaseModel
from schematics.types import IntType, StringType
from schematics.types.compound import ListType
from schematics.exceptions import ValidationError, ModelConversionError


class ItemModel(BaseModel):
    """
    Модель для товаров
    """
    MONGO_COLLECTION = 'items'  #: Имя коллекции в DB
    name = StringType(required=True)  #: название объекта (required)
    images = ListType(StringType())  #: список картинок
    tags = ListType(StringType())  #: список тегов
    cost = IntType(default=0)  #: стоимость
    sale_cost = IntType(default=0)  # стоимость со скидкой
    category = StringType(required=True)  # категория товара (required)


class CategoryModel(BaseModel):
    """
    Модель для категорий товаров
    """
    MONGO_COLLECTION = 'categories'  #: Имя коллекции в DB
    name = StringType(required=True)  #: название объекта (required)
    rus_name = StringType()  #: название объекта на русском
    parent = StringType(default='')  # родительская категория (если есть)
    info = StringType(default='')  # описание категории (у родительсикх категорий отсутствуюет)

    def get_categories(self):
        """
        Возвращает все категории в виде структуры, в формате:
        [
            {
                parent_category,
                sub_categories:
                [
                    {category}, {category}
                ]
            },
            {
                parent_category,
                sub_categories:
                [
                    {category}, {category}
                ]
            }
        ]
        :return:
        """
        pass


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