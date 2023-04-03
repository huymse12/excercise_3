import model
from abc import ABC, abstractmethod


class IPostRepository(ABC):
    @abstractmethod
    def create_post(self, entity):
        pass

    @abstractmethod
    def list_post(self):
        pass

    @abstractmethod
    def update_post(self, post_id, entity):
        pass

    @abstractmethod
    def delete_post(self, post_id):
        pass

    @abstractmethod
    def get_detail_post(self, post_id):
        pass


class PostRepository(IPostRepository):
    def __init__(self, mysql_db):
        self._mysql_db = mysql_db

    def create_post(self, entity):
        try:
            sql = "insert into posts(created, title, content) VALUES (CURRENT_TIME ,%s,%s)"
            value = (entity.title, entity.content)
            cursor = self._mysql_db.cursor()
            cursor.execute(sql, value)
            self._mysql_db.commit()
        except:
            return "Internal Error"

    def list_post(self):
        try:
            sql = "select * from posts"
            cursor = self._mysql_db.cursor()
            cursor.execute(sql)
            data = cursor.fetchall()
            return data
        except Exception as e:
            print(e)
            return None

    def update_post(self, post_id, entity):
        try:
            arr_query = []
            value = []
            if entity.title is not None:
                arr_query.append("title = %s")
                value.append(entity.title)

            if entity.content is not None:
                arr_query.append("content = %s")
                value.append(entity.content)
            if len(arr_query) > 0:
                sql = "update posts set {} where id = {}".format(",".join(arr_query), post_id)
                cursor = self._mysql_db.cursor()
                cursor.execute(sql, value)
                self._mysql_db.commit()
            return True
        except Exception as e:
            print(e)

    def delete_post(self, post_id):
        try:
            sql = "delete from posts where id = {}".format(post_id)
            cursor = self._mysql_db.cursor()
            cursor.execute(sql)
            self._mysql_db.commit()
        except Exception as e:
            print(e)

    def get_detail_post(self, post_id):
        sql = "select * from posts where id = {}".format(post_id)
        cursor = self._mysql_db.cursor()
        cursor.execute(sql)
        data = cursor.fetchone()
        return data
