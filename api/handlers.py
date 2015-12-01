import os
import json
import base64
import logging
from tornado import gen
from api.models import ItemModel
from base.handlers import BaseHandler
from bson.objectid import ObjectId
from bson.errors import InvalidId
from settings import *

l = logging.getLogger(__name__)

# class JSONEncoder(json.JSONEncoder):
# def default(self, o):
# if isinstance(o, ObjectId):
#             return str(o)
#         return json.JSONEncoder.default(self, o)


class ItemHandler(BaseHandler):
    """
    Класс для обработки запросов создание/удаление/редактирование предметов каталога
    """

    def initialize(self, **kwargs):
        super(ItemHandler, self).initialize(**kwargs)
        self.db = self.settings['db']

    @gen.coroutine
    def get(self, _id):
        """
        Возвращает объект с указанным _id
        :param _id: id объекта
        :return: объект в виде словаря. None - если не найден
        """
        try:
            _id = ObjectId(_id)
        except InvalidId as error:
            return self.render_json({"error": str(error)})
        item = yield ItemModel.find_one(self.db, {"_id": _id})
        return self.render_json(item)

    @gen.coroutine
    def post(self, _id):
        """Создает

        :param _id:
        :type _id: str
        :return:
        :raises:
        """
        item = ItemModel(self.json, db=self.db)  # FIXME: db = self.db is bad -(
        # item.set_db(self.db)
        yield item.save()
        if item.errors:
            return self.render_json(item.errors)
        return self.render_json(item)

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