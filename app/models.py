import datetime, re
from app import db

def slugify(s):
    return re.sub('[^\w]+', '-', s).lower() 

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    slug = db.Column(db.String(100), unique=True)
    body = db.Column(db.Text)
    created_timestamp = db.Column(db.DateTime, default=datetime.datetime.now)
    modified_timestamp = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    def __inti__(self, *args, **kwargs):
        super(Entry, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        self.slug = ''
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return '<Entry: %s>' % self.title

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.column(db.string(64))
    slug = db.Column(sb.String(64), unique=True)

    def __inti__(self, *args, **kwargs):
        super(Tag, self).__inti__(*args, **kwargs)
        self.slug = slug(self.name)

    def __repr__(self):
        return '<Tag %s>' % self.name
