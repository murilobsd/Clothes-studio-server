import os
import json
import base64
import logging
from tornado import gen
from api.models import ItemModel
from base.handlers import BaseHandler
from bson.objectid import ObjectId
from schematics.exceptions import ModelConversionError, ModelValidationError
from settings import *

l = logging.getLogger(__name__)

# class JSONEncoder(json.JSONEncoder):
# def default(self, o):
#         if isinstance(o, ObjectId):
#             return str(o)
#         return json.JSONEncoder.default(self, o)


class ItemHandler(BaseHandler):
    """
    Класс для обработки запросов создание/удаление/редактирование предметов каталога
    """

    def initialize(self, **kwargs):
        super(ItemHandler, self).initialize(**kwargs)
        self.db = self.settings['db']

    def get(self, _id):
        """
        Возвращает объект с указанным _id
        :param _id: id объекта
        :return: объект в виде словаря. None - если не найден
        """
        print('category =', _id)
        self.write('GET: OK')

    @gen.coroutine
    def post(self, _id):
        """Создает

        :param _id:
        :type _id: str
        :return:
        :raises:
        """
        print('id = ', _id)
        print('json -->', self.json)
        item = ItemModel(self.json, db=self.db)
        # item.set_db(self.db)
        item, errors = yield item.save()
        if errors:
            self.render_json(errors)
            print('errors = ', errors)
        print('item =', item.to_primitive())
        self.render_json(item.to_primitive())

        # self.render_json({"result": "OK"})

    def put(self, _id):
        pass


class UploadHandler(BaseHandler):
    SUPPORTED_METHODS = ("CONNECT", "GET", "HEAD", "POST", "DELETE", "PATCH", "PUT", "OPTIONS")

    def initialize(self, **kwargs):
        super(UploadHandler, self).initialize(**kwargs)

    def options(self, *args, **kwargs):
        pass

    def get(self):
        print("GET ok")
        self.render_json({"result": "OK"})

    def post(self):
        file_info = self.json
        file_name = file_info['filename']
        with open(location(settings['upload_path'] + file_name), 'wb') as f:
            f.write(base64.b64decode(file_info['base64']))

        self.render_json({"result": "OK"})