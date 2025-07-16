import os
from flask import Blueprint, render_template, request, redirect, url_for, session, abort, current_app
from werkzeug.utils import secure_filename
from models import db, Country, EventType, Event, User

routes = Blueprint('routes', __name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

@routes.route('/', methods=['GET', 'POST'])
def index():
    countries = Country.query.all()
    event_types = EventType.query.all()

    print(countries)
    print(event_types)

    selected_country = request.form.get('country')
    selected_event_type = request.form.get('event_type')

    events_query = Event.query

    if selected_country:
        selected_country = int(selected_country)
        events_query = events_query.filter_by(country_id=selected_country)

    if selected_event_type:
        selected_event_type = int(selected_event_type)
        events_query = events_query.filter_by(event_type_id=selected_event_type)

    events = events_query.all()

    for event in events:
        print(event.id_event)

    return render_template('index1.html', 
                            countries=countries, 
                            event_types=event_types, 
                            events=events, 
                            selected_country=selected_country, 
                            selected_event_type=selected_event_type)


@routes.route('/auth')
def auth():
    return render_template('index2.html')


@routes.route('/profile')
def profile():
    print(f"session['id_user']: {session.get('id_user')}")  
    
    if 'id_user' not in session:
        return redirect(url_for('routes.index'))  

    user = User.query.get(session['id_user'])
    return render_template('index5.html', user=user)  


@routes.route('/about/<id_event>')
def about(id_event):
    print(f"Отримано id_event: {id_event}")
    event = Event.query.get(id_event)
    if not event:
        abort(404, description="Подію не знайдено")

    return render_template('index4.html', event=event, id_event=id_event)


@routes.route('/upload_image/<id_event>', methods=['POST'])
def upload_image(id_event):
    if 'file' not in request.files:
        return 'Файл не знайдений'
    
    file = request.files['file']
    
    if file.filename == '':
        return 'Немає вибраного файлу'
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(routes.config['UPLOAD_FOLDER'], filename))
        
        event = Event.query.get(id_event)
        event.event_image = f'img/{filename}'  
        db.session.commit()
        
        return f'Зображення для заходу {event.title} успішно завантажено!'


@routes.route('/register', methods=['POST'])
def register():
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    email = request.form.get('email')
    password = request.form.get('password')
    phone = request.form.get('phone')
    role = request.form.get('role')  
    org_name = request.form.get('org_name')  

    new_user, error = User.register_user(firstname, lastname, email, password, phone, role, org_name)
    if error:
        return error, 400

    session['id_user'] = new_user.id_user  
    session['user_role'] = new_user.get_roles()

    return redirect(url_for('routes.profile'))


@routes.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    user, error = User.login_user(email, password)
    if error:
        return error, 400

    session['id_user'] = user.id_user
    session['user_role'] = user.get_roles()

    return redirect(url_for('routes.profile'))


@routes.route('/logout', methods=['GET'])
def logout():
    if 'id_user' in session:
        User.log_out()
        return redirect(url_for('routes.index')) 
    return redirect(url_for('routes.index'))


@routes.route('/delete_user', methods=['POST'])
def delete_user():
    if 'id_user' not in session:
        return redirect(url_for('routes.index'))  

    user_id = session['id_user']
    user = User.query.get(user_id)

    if user:
        db.session.delete(user)  
        db.session.commit()
        session.pop('id_user')  
        return redirect(url_for('routes.index'))  
    else:
        return "Користувача не знайдено", 404
        

@routes.route('/confirm_delete', methods=['GET'])
def confirm_delete():
    if 'id_user' not in session:
        return redirect(url_for('routes.index'))  
    
    return render_template('index6.html')  