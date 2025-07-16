from flask_sqlalchemy import SQLAlchemy
from flask import session
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

class Country(db.Model):
    __tablename__ = 'country'
    id_country = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country_name = db.Column(db.String(15), unique=True, nullable=False)
    
    events = db.relationship('Event', back_populates='country', lazy=True)

    @staticmethod
    def filter_events_by_country(country_id):
        return Event.query.filter_by(country_id=country_id).all()

    def __repr__(self):
        return self.country_name


class EventType(db.Model):
    __tablename__ = 'event_type'
    id_event_type = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_type_name = db.Column(db.String(50), unique=True, nullable=False)
    
    events = db.relationship('Event', back_populates='event_type', lazy=True)

    @staticmethod
    def filter_events_by_type(event_type_id):
        return Event.query.filter_by(event_type_id=event_type_id).all()

    def __repr__(self):
        return self.event_type_name


class Role(db.Model):
    __tablename__ = 'role'
    id_role = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_name = db.Column(db.String(15), unique=True, nullable=False)

    user_roles = db.relationship('UserRoles', backref='role', lazy=True)

    def __repr__(self):
        return self.role_name


class FormationOrg(db.Model):
    __tablename__ = 'formation_org'
    id_form = db.Column(db.Integer, primary_key=True, autoincrement=True)
    form_name = db.Column(db.String(160), nullable=False)
    users_form = db.relationship('User', back_populates = 'formation_org', lazy=True)

    def __repr__(self):
        return self.form_name


class User(db.Model):
    __tablename__ = 'user'
    id_user = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    user_password = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(9), nullable=False)
    
    formation_id = db.Column(db.Integer, db.ForeignKey('formation_org.id_form'), nullable=True)
    
    formation_org = db.relationship('FormationOrg', back_populates='users_form', lazy=True)
    roles = db.relationship(
        'Role',
        secondary='user_roles',
        backref=db.backref('users_roles', lazy=True),
        lazy=True
    )

    def get_roles(self):
        return [role.role_name for role in self.roles]

    def check_password(self, password):
        return bcrypt.check_password_hash(self.user_password, password)
    
    @staticmethod
    def register_user(first_name, last_name, email, password, phone, role, org_name=None):
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return None, "Користувач із такою електронною поштою вже існує"

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        new_user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            user_password=hashed_password,
            phone=phone
        )
        db.session.add(new_user)
        db.session.commit()

        role_entry = Role.query.filter_by(role_name=role.lower()).first()
        if not role_entry:
            return None, "Роль не знайдена в базі даних"
        role_id = role_entry.id_role
        user_role = UserRoles(user_id=new_user.id_user, role_id=role_id)
        db.session.add(user_role)

        if org_name:
            formation = FormationOrg.query.filter_by(form_name=org_name).first()
            if not formation:
                formation = FormationOrg(form_name=org_name)
                db.session.add(formation)
                db.session.commit()
            new_user.formation_id = formation.id_form

        db.session.commit()
        return new_user, None
    
    @staticmethod
    def login_user(email, password):
        user = User.query.filter_by(email=email).first()
        if not user or not bcrypt.check_password_hash(user.user_password, password):
            return None, "Неправильна електронна пошта або пароль"
        return user, None

    @staticmethod
    def log_out():
        session.pop('id_user', None)
        session.pop('user_role', None)
        session.clear()

    def __repr__(self):
        return f"<User {self.first_name} {self.last_name} ({self.email})>"


class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id_user'), primary_key=True, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id_role'), primary_key=True, nullable=False)


class Event(db.Model):
    __tablename__ = 'event'
    id_event = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(150), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=True)
    location = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Numeric(6, 2), nullable=False)
    currency = db.Column(db.String(3), nullable=False)
    age_category = db.Column(db.String(15), nullable=False)
    transportation = db.Column(db.String(200), nullable=True)
    application = db.Column(db.String(500), nullable=True)
    description = db.Column(db.Text, nullable=True)
    event_image = db.Column(db.String(255), nullable=True)

    country_id = db.Column(db.Integer, db.ForeignKey('country.id_country'), nullable=False)
    event_type_id = db.Column(db.Integer, db.ForeignKey('event_type.id_event_type'), nullable=False)
    organizer_id = db.Column(db.Integer, db.ForeignKey('user.id_user'), nullable=True)

    country = db.relationship('Country', back_populates='events', lazy=True)
    event_type = db.relationship('EventType', back_populates='events', lazy=True)
    user = db.relationship('User', backref='events', lazy=True)

    def get_event_description(self):
        return f"Event: {self.title} | Location: {self.location}"