from flask import Flask
from flask import request, json
import mysql.connector
import repository
import services

app = Flask(__name__)


def connect_my_sql():
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345678',
        database="PostDB"
    )
    return mydb


mysql_db = connect_my_sql()
postRepository = repository.PostRepository(mysql_db)
postService = services.PostService(postRepository)


@app.route("/api/posts", methods=["POST"])
def create_post():
    req = request.json
    return postService.create_post(req)


@app.route("/api/posts", methods=["GET"])
def list_post():
    return postService.get_list_post_by_id()


@app.route("/api/posts/<post_id>", methods=["PUT"])
def edit_post(post_id):
    req = request.json
    return postService.edit_post_by_id(post_id, req)


@app.route("/api/posts/<post_id>", methods=["DELETE"])
def delete_post(post_id):
    return postService.delete_post_by_id(post_id)


@app.route("/api/posts/<post_id>", methods=["GET"])
def get_detail_post(post_id):
    return postService.get_post_by_id(int(post_id))


app.run("127.0.0.1", 3000)
