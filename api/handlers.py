import os
import json
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
    def initialize(self, **kwargs):
        super(UploadHandler, self).initialize(**kwargs)

    def post(self):
        fileinfo = self.request.files['filearg'][0]
        print("fileinfo is", fileinfo)
        fname = fileinfo['filename']
        # extn = os.path.splitext(fname)[1]
        # cname = str(uuid.uuid4()) + extn
        # f = open(location(settings['upload_path'] + fname), 'w')
        with open(location(settings['upload_path'] + fname), 'wb') as f:
            f.write(fileinfo['body'])
        # self.finish(cname + " is uploaded!! Check %s folder" %__UPLOADS__)

        self.render_json({"result": "OK"})