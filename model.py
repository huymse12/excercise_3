class Post(object):
    def __init__(self, post_id, created_date, title, content):
        self.title = title
        self.content = content
        self.id = post_id
        self.created_date = created_date


class ResponseAPI(object):
    def __init__(self, code, message, data):
        self.code = code
        self.message = message
        self.data = data


def success_response(data):
    return ResponseAPI(200, "Success", data)


def bad_request_response(message):
    return ResponseAPI(404, message, None)


def internal_error_response(message):
    return ResponseAPI(500, message, None)
