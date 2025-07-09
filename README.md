# Weather Query Web Application

### 1. Technology Stack
- **Language**: Python  
- **Web Framework**: Django  
- **Database**: PostgreSQL  
- **Weather API**: OpenWeatherMap
- **Frontend**: Django Templates + Bootstrap 5  
- **Environment Management**: Docker, Docker Compose
- **Tests**: Django TestCase 

### 2. Functionality
- **User inputs a city name on the main page.**
- **On form submission:**
  - The app fetches current weather data from the OpenWeatherMap API.
  - Saves the query details to PostgreSQL: city, timestamp, temperature, feels like, pressure, humidity, wind speed, and weather description.
  - Displays the query history on the same page with city, weather details, and timestamp.

### 3. Additional Features
- Admin panel enabled for managing stored queries.
- Unit tests cover models, views, and forms.
- Docker setup included for easy environment configuration.

### 4. Setup Instructions

# Prerequisites
- Docker
- Docker Compose
- OpenWeatherMap API key (free tier available at [openweathermap.org](https://openweathermap.org/))

# 1. Clone the repository:
`git clone https://github.com/antasia03/weather_project`

`cd weather_project`

# 2. Create .env file with the following variables:
`DB_NAME=weather_db`

`DB_USER=postgres`

`DB_PASSWORD=yourpassword`

`DB_HOST=db`

`DB_PORT=5432`

`OPENWEATHER_API_KEY=your_api_key_here`

`SECRET_KEY=your_django_secret_key`

`DEBUG=True`

# 3. Build and start Docker containers:

`docker-compose up --build`

# 4. Apply migrations and create a superuser for admin access:

`docker-compose run web python manage.py migrate`

`docker-compose run web python manage.py createsuperuser`

# 5. Access:

Access the app at http://localhost:8000

Access the admin panel at http://localhost:8000/admin and log in with the superuser credentials.

# 6. To run tests inside the container:

`docker-compose run web python manage.py test`
