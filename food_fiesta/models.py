from food_fiesta import db


class Category(db.Model):
    '''schema for the Category model'''
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)

    def __repr__(self):
        '''return itself as a string'''
        return self.category_name


class Users(db.Model):
    '''schema for the Users model'''
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    is_superuser = db.Column(db.Boolean, unique=False, default=False)

    def __repr__(self):
        '''return itself as a string'''
        return self.user_name
