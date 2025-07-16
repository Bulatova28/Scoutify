function showAccountType(action) {
    document.getElementById('actionButtons').style.display = 'none';
    document.querySelector('h3').style.display = 'none'; 
    document.getElementById('roleButtons').style.display = 'block';
    document.getElementById('roleHeader').style.display = 'block';

    if (action === 'login') {
        document.getElementById('roleButtons').innerHTML = `
            <button type="button" onclick="showLoginForm('Скаут')">Скаут</button>
            <button type="button" onclick="showLoginForm('Організатор')">Організатор</button>
        `;
    } else {
        document.getElementById('roleButtons').innerHTML = `
            <button type="button" onclick="showForm('Скаут')">Скаут</button>
            <button type="button" onclick="showForm('Організатор')">Організатор</button>
        `;
    }
}

function sendRegisterForm(role) {
    const formData = new FormData(document.querySelector('#mainForm'));
    formData.append('role', role);

    fetch('/register', {
    method: 'POST',
    body: formData
	})
	.then(response => {
	    if (!response.ok) {
	        return response.text(); // Читаємо текст помилки
	    }
	    window.location.href = "/profile";
	})
	.then(error => {
	    if (error) {
	        alert('Помилка реєстрації. Перевірте дані: ' + error);
	    }
	})
	.catch(err => {
	    console.error("Error: ", err);
	    alert("Щось пішло не так.");
	});
}

function sendLoginForm() {
    const formData = new FormData(document.querySelector('#mainForm'));

    fetch('/login', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            alert('Неправильна електронна пошта або пароль.');
        } else {
            window.location.href = "/profile";
        }
    });
}



function showForm(role) {
	document.getElementById('roleButtons').style.display = 'none';
	document.getElementById('roleHeader').style.display = 'none'; 

	const formFields = document.getElementById('formFields');
	
	if (role === 'Скаут') {
		formFields.innerHTML = `
			<h3>Реєстрація - Скаут</h3>
			<label for="firstname">Ім'я</label><br>
			<input class="input" type="text" name="firstname" placeholder="Анастасія"><br>

			<label for="lastname">Прізвище</label><br>
			<input class="input" type="text" name="lastname" placeholder="Кропивницька"><br>

			<label for="email">Електронна пошта</label><br>
			<input class="input" type="email" name="email" placeholder="anastasiakrop@gmail.com"><br>

			<label for="phone">Телефон</label><br>
			<input class="input" type="text" name="phone" placeholder="50 222 45 65"><br>

			<label for="password">Пароль</label><br>
			<input class="input" type="password" name="password" placeholder="********"><br>

			<label for="org_name">Назва формування</label><br>
			<input class="input" type="text" name="org_name" placeholder="Сарматівці"><br>

			<div class="button-box">
				<input class="button" type="submit" value="Sign up" onclick="sendRegisterForm('Скаут')">
			</div>
		`;
	} 

	else if (role === 'Організатор') {
		formFields.innerHTML = `
			<h3>Реєстрація - Організатор</h3>
			<label for="firstname">Ім'я</label><br>
			<input class="input" type="text" name="firstname" placeholder="Анастасія"><br>

			<label for="lastname">Прізвище</label><br>
			<input class="input" type="text" name="lastname" placeholder="Кропивницька"><br>

			<label for="email">Електронна пошта</label><br>
			<input class="input" type="email" name="email" placeholder="anastasiakrop@gmail.com"><br>

			<label for="phone">Телефон</label><br>
			<input class="input" type="text" name="phone" placeholder="50 222 45 65"><br>

			<label for="password">Пароль</label><br>
			<input class="input" type="password" name="password" placeholder="********"><br>

			<label for="org_name">Назва формування</label><br>
			<input class="input" type="text" name="org_name" placeholder="Сарматівці"><br>

			<div class="button-box">
				<input class="button" type="submit" value="Sign up" onclick="sendRegisterForm('Організатор')">
			</div>
		`;
	}

	document.querySelector('h3').style.display = 'none';
	formFields.style.display = 'block';
}

function showLoginForm(role) {
	document.getElementById('roleButtons').style.display = 'none';
	document.getElementById('roleHeader').style.display = 'none';

	const formFields = document.getElementById('formFields');
	
	if (role === 'Скаут') {
		formFields.innerHTML = `
			<h3>Вхід - Скаут</h3>
			<label for="email">Електронна пошта</label><br>
			<input class="input" type="email" name="email" placeholder="anastasiakrop@gmail.com"><br>

			<label for="password">Пароль</label><br>
			<input class="input" type="password" name="password" placeholder="********"><br>

			<div class="button-box">
				<input class="button" type="submit" value="Login" onclick="sendLoginForm()">
			</div>
		`;
	} 

	else if (role === 'Організатор') {
		formFields.innerHTML = `
			<h3>Вхід - Організатор</h3>
			<label for="email">Електронна пошта</label><br>
			<input class="input" type="email" name="email" placeholder="anastasiakrop@gmail.com"><br>

			<label for="password">Пароль</label><br>
			<input class="input" type="password" name="password" placeholder="********"><br>

			<div class="button-box">
				<input class="button" type="submit" value="Login" onclick="sendLoginForm()">
			</div>
		`;
	}

	document.querySelector('h3').style.display = 'none';
	formFields.style.display = 'block';
}

function redirectToIndex() {
	window.location.href = "{{ url_for('profile') }}"; 
}