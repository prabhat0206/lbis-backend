from . import db


class Events(db.Model):
    eid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image_url = db.Column(db.String)
    isVideo = db.Column(db.Boolean, default=False)


class Notice(db.Model):
    nid = db.Column(db.Integer, primary_key=True)
    notice = db.Column(db.String)
    description = db.Column(db.String)

