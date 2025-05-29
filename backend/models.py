from config import db

class User(db.Model):   # Creating the Table
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)

    def to_json(self):  # used to pass to api [Javascript Object Notation]
        return {
            "id":self.id,
            "firstName":self.first_name,    #json = camelCase | python = snake_case
            "lastName":self.last_name,
            "email":self.email
        }