from quart import Blueprint,request,jsonify
from models.Post import Post
from db.database import get_db
from sqlalchemy import select,update,delete
from sqlalchemy.exc import NoResultFound

post_bp = Blueprint("Post",__name__)



#create
@post_bp.route("/create",methods=["POST"])
async def create_user():
    data = await request.get_json()
    if not data:
        return jsonify({"error": "No JSON body found"}), 400
    
    title = data.get("title")
    content = data.get("content")
    user_id = data.get("user_id")
    
    if not title or not content or not user_id:
        return jsonify({"error": "Missing required fields"}), 400
    
    async for session in get_db():
        post = Post(title=title,content=content,user_id=user_id)
        session.add(post)
        await session.commit()
        await session.refresh(post)
        return jsonify({"id": post.id, "title": post.title, "content": post.content,"user_id":post.user_id}),201


#Read All
@post_bp.route("/all",methods=["GET"])
async def get_posts():
    async for session in get_db():
        result = await session.execute(select(Post))
        posts = result.scalars().all()
        return jsonify([
            {"id":p.id,"title":p.title,"content":p.content,"user_id":p.user_id}
            for p in posts
        ])