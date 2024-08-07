# Django Itinerary Planner

This Django project generates itineraries based on the city and number of days inputted by the user. The itineraries include recommendations for hotels, restaurants, and places to visit. The project uses machine learning to recommend the best options based on user preferences.

## Features

- Recommend hotels, restaurants, and places to visit based on the city and number of days.
- Uses machine learning models to generate recommendations.
- Generates an organized itinerary for each day.

## Installation

1. **Fork the repository** to your GitHub account.

2. **Clone your forked repository** to your local machine:

    ```sh
    git clone [https://github.com/Vivek-Jadhav27/tripeaze_api.git]
    cd tripeaze
    ```
3. **Install the dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Run the migrations** to set up the database:

    ```sh
    python manage.py migrate
    ```

5. **Create a superuser** to access the Django admin:

    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server**:

    ```sh
    python manage.py runserver
    ```

## Usage

Once the server is running, you can access the following URL patterns:

### Web Interface

- **URL:** `/itinerary_view/`
- **Description:** Displays a form to enter the city and number of days to generate an itinerary.

### API Endpoint

- **URL:** `/api/`
- **Method:** POST
- **Description:** API endpoint to generate an itinerary based on the provided data.

#### Example Request

To generate an itinerary using the API endpoint, send a POST request with the following JSON payload:

```json
{
  "city": "Mumbai",
  "num_days": 2
}
