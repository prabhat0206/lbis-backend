from flask import Blueprint, request, abort
from flask_restful import Resource, Api
from sqlalchemy import delete
from .models import *
from functools import wraps
from .aws import upload_file_to_s3
from werkzeug.security import check_password_hash, generate_password_hash
from .config import ADMIN_EMAIL, ADMIN_PASSWORD


def check_admin(next):
    @wraps(next)
    def authorize(*args, **kwargs):
        token = request.headers.get('Authorization').replace("Bearer ", "")
        if token:
            if check_password_hash(token, ADMIN_EMAIL+ADMIN_PASSWORD):
                return next(*args, **kwargs)
            else:
                abort(401)
        else:
            abort(401)
    return authorize


admin_api = Blueprint('admin_api', __name__)
api = Api(admin_api)


class Login(Resource):

    def post(self):
        data = request.get_json()
        if data['email'] == ADMIN_EMAIL and data['password'] == ADMIN_PASSWORD:
            return {"Success": True, "token": generate_password_hash(ADMIN_EMAIL+ADMIN_PASSWORD)}
        else:
            abort(401)


class GallerHandler(Resource):

    @check_admin
    def post(self):
        data = request.form
        file = request.files.get('image')
        url = upload_file_to_s3(file)
        new_gallery = Events(name=data['name'], image_url=url)
        db.session.add(new_gallery)
        db.session.commit()
        if 'image' in file.mimetype:
            new_gallery.isVideo = False
        else:
            new_gallery.isVideo = True
        db.session.commit()
        return {"Success": True}
    
    @check_admin
    def delete(self):
        data = request.args
        gallery = Events.query.filter_by(eid=int(data.get('eid'))).first()
        db.session.delete(gallery)
        db.session.commit()
        return {"Success": True}
    


class NoticeHandler(Resource):
    
    @check_admin
    def post(self):
        data = request.get_json()
        new_Notice = Notice(notice=data['title'], description=data['description'])
        db.session.add(new_Notice)
        db.session.commit()
        return {"Success": True}
    

    @check_admin
    def delete(self):
        data = request.args
        notice = Notice.query.filter_by(nid=int(data.get('nid'))).first()
        db.session.delete(notice)
        db.session.commit()
        return {"Success": True}


class AddSlide(Resource):

    @check_admin
    def post(self):
        data = request.form
        url = upload_file_to_s3(request.files.get('image'))
        new_Slide = Slide(name=data['name'], url=url)
        db.session.add(new_Slide)
        db.session.commit()
        return {"Success": True}
    
    @check_admin
    def delete(self):
        data= request.args
        slide = Slide.query.filter_by(sid=int(data['sid'])).first()
        db.session.delete(slide)
        db.session.commit()
        return {"Success": True}


api.add_resource(GallerHandler, '/gallery')
api.add_resource(Login, '/login')
api.add_resource(NoticeHandler, '/notice')
api.add_resource(AddSlide, '/slide')