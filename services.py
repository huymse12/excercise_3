from abc import ABC, abstractmethod
import model
import repository


class IPostService(ABC):

    @abstractmethod
    def create_post(self, request):
        pass

    @abstractmethod
    def get_post_by_id(self, post_id):
        pass

    @abstractmethod
    def edit_post_by_id(self, post_id, request):
        pass

    @abstractmethod
    def delete_post_by_id(self, post_id):
        pass

    @abstractmethod
    def get_list_post_by_id(self):
        pass


class PostService(IPostService):

    def __init__(self, post_repository: repository.IPostRepository):
        self._post_repository = post_repository

    def create_post(self, request):
        try:
            post = model.Post(0, None, request["title"], request["content"])
            self._post_repository.create_post(post)
            return model.success_response("Success").__dict__
        except Exception as e:
            print(e)
            return model.internal_error_response("Internal Error").__dict__

    def get_post_by_id(self, post_id):
        try:
            data = self._post_repository.get_detail_post(post_id)
            if data is None:
                return model.bad_request_response("Không tìm thấy bài post").__dict__
            return model.success_response(model.Post(data[0], data[1], data[2], data[3]).__dict__).__dict__
        except Exception as e:
            print(e)
            return model.internal_error_response("Internal Error").__dict__

    def edit_post_by_id(self, post_id, request):
        try:
            post_entity = self._post_repository.get_detail_post(post_id)
            if post_entity is None:
                return model.bad_request_response("Post not found").__dict__
            title = None
            content = None
            if "title" in request:
                title = request["title"]

            if "content" in request:
                content = request["content"]
            entity_update = model.Post(0, None, title, content)
            self._post_repository.update_post(post_id, entity_update)
            return model.success_response("Success").__dict__
        except Exception as e:
            print(e)
            return model.internal_error_response("Internal Error").__dict__

    def delete_post_by_id(self, post_id):
        try:
            data = self._post_repository.get_detail_post(post_id)
            if data is None:
                return model.bad_request_response("Post not found").__dict__
            self._post_repository.delete_post(post_id)
            return model.success_response("Delete success").__dict__
        except Exception as e:
            print(e)
            return model.internal_error_response("Internal Error").__dict__

    def get_list_post_by_id(self):
        try:
            data_posts = self._post_repository.list_post()
            response = []
            for post in data_posts:
                response.append(model.Post(post[0], post[1], post[2], post[3]).__dict__)
            return model.success_response(response).__dict__
        except Exception as e:
            print(e)
            return model.internal_error_response("Internal Error").__dict__
