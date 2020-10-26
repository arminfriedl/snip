from . import db


class Snip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(512), nullable=False)
    snip = db.Column(db.String(16), unique=True, nullable=False, index=True)
    reusable = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f"<Snip .url={self.url}, .snip={self.snip}"
