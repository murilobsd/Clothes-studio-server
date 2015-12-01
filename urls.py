from tornado.web import url

from api.handlers import ItemHandler, UploadHandler


url_patterns = [
    # url(r"/", BaseHandler, name="home"),
    # url(r"/api/items/([0-9a-z]+)/", RegisterHandler),
    url(r"^/api/item/([0-9a-z]*)/*", ItemHandler),
    url(r"^/api/upload/img", UploadHandler),
]
