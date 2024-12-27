// Функция для установки темы
function setTheme(isDark) {
	const navbar = document.getElementById('main-navbar');
	const themeIcon = document.getElementById('theme-icon');
	
	if (isDark) {
			navbar.classList.remove('is-light');
			navbar.classList.add('is-dark');
			themeIcon.classList.remove('fa-sun');
			themeIcon.classList.add('fa-moon');
	} else {
			navbar.classList.remove('is-dark');
			navbar.classList.add('is-light');
			themeIcon.classList.remove('fa-moon');
			themeIcon.classList.add('fa-sun');
	}
	
	// Сохраняем состояние темы в localStorage
	localStorage.setItem('isDarkTheme', isDark);
}

// Функция переключения темы
function toggleTheme() {
	const navbar = document.getElementById('main-navbar');
	const isDark = navbar.classList.contains('is-dark');
	setTheme(!isDark);
}

// При загрузке страницы проверяем сохраненную тему
document.addEventListener('DOMContentLoaded', () => {
	const savedTheme = localStorage.getItem('isDarkTheme');
	if (savedTheme !== null) {
			setTheme(savedTheme === 'true');
	}
});
