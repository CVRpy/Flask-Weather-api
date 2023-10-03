# Flask-Weather-api

The Flask City Weather App is a simple web application that allows users to fetch weather data for a city using the OpenWeatherMap API. This README provides instructions on how to use the app and contribute to its development.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Documentation](#documentation)
- [License](#license)

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- [OpenWeatherMap API key](https://openweathermap.org/appid)

### Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/CVRpy/Flask-Weather-api.git
   cd Flask-Weather-api
   ```

2. Create a virtual environment and activate it:

   ```shell
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate
   ```

3. Install the required packages:

   ```shell
   pip install -r requirements.txt
   ```

4. Set your OpenWeatherMap API key as an environment variable:

   ```shell
   export OPENWEATHERMAP_API_KEY="your_api_key_here"
   ```

## Usage

1. Start the Flask app:

   ```shell
   python app.py
   ```

2. Open your web browser and navigate to `http://localhost:5000/`.

3. Enter the name of a city in the input field and click "Get Weather."

4. The app will display the temperature and weather description for the specified city.

## Contributing

We welcome contributions to improve the Flask City Weather App. To contribute, follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch from the `main` branch for your feature or bugfix:
   ```shell
   git checkout -b feature/your-feature-name
   ```
3. Make your changes and commit them.
4. Push your branch to your forked repository on GitHub.
5. Create a Pull Request (PR) from your branch to the `main` branch of this repository.
6. Describe your changes and why they should be merged.

Our team will review your PR, provide feedback, and merge it if approved.

## Documentation

Documentation for this project is generated using Sphinx. To generate and view the documentation locally, follow these steps:

1. Run the documentation generation script:

   ```shell
   python generate_docs.py
   ```

2. Open the generated documentation in your web browser. It is located in the `docs/build` directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to customize this README to fit the specific details and needs of your Flask City Weather App project. Including clear instructions for installation, usage, and contributing will make it easier for developers to understand and work with your project.
