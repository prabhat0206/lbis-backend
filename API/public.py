from flask import Blueprint, request, render_template
from flask_restful import Resource, Api
from .models import *
from . import get_model_dict, mail
from flask_mail import Message

public_api = Blueprint('public_api', __name__)
api = Api(public_api)


class AllNotice(Resource):

    def get(self):
        notices = Notice.query.order_by(Notice.nid.desc()).all()
        all_notice = []
        for notice in notices:
            all_notice.append(get_model_dict(notice))
        return {"Success": True, "Notices": all_notice}
        

class Gallery(Resource):

    def get(self):
        gallery = Events.query.order_by(Events.eid.desc()).all()
        all_image_videos = []

        for image_video in gallery:
            all_image_videos.append(get_model_dict(image_video))

        return {"Success": True, "Gallery": all_image_videos}


class Contact(Resource):
    
    def post(self):
        data = request.get_json()
        msg = Message(
            'Question/Query from lordbuddhaschool.in',
            sender="noreply@lordbuddaschool.in",
            recipients=[data['email']]
        )
        _request_email = data['email']
        _request_name = data['name']
        _request_phone = data['phone']
        _request_message = data['message']
        msg.html = render_template('email.html', email=_request_email, name=_request_name, phone=_request_phone, message=_request_message)
        mail.send(msg)
        return {"Success": True}


api.add_resource(AllNotice, '/notice')
api.add_resource(Gallery, '/gallery')
api.add_resource(Contact, '/contact')
