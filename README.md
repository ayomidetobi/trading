# Trading Project

This project is a trading application that allows users to manage and track their trades and analyze their profit/loss. It provides features for creating trades, viewing trade history, calculating total profit/loss, and visualizing trade data on a chart.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Features

- User authentication: Users can create an account, log in, and log out to access the trading application.
- Trade creation: Users can create new trades by specifying the trade details, such as entry price, exit price, and quantity.
- Trade history: Users can view their trade history, including details like profit/loss, timestamp, and trade duration.
- Profit/Loss analysis: The application calculates the total profit/loss for all trades and displays it to the user.
- Chart visualization: The application provides a chart to visualize the trade data, allowing users to analyze their trading performance over time.

## Installation

1. Clone the repository: `git clone https://github.com/ayomidetobi/trading.git`
2. Navigate to the project directory: `cd trading-project`
3. Install dependencies: `pip install -r requirements.txt`
4. Set up the database:
   - Create a PostgreSQL database.
   - Update the database configuration in the settings file.
   - Run database migrations: `python manage.py migrate`
5. Start the development server: `python manage.py runserver`
6. Access the application at: `http://localhost:8000`

## Usage

1. Create an account or log in using your existing credentials.
2. Navigate to the trade creation page and enter the details of your trades.
3. View your trade history and analyze your profit/loss.
4. Explore the chart visualization to gain insights into your trading performance.

## Technologies Used

- Python
- Django
- PostgreSQL
- HTML
- CSS
- JavaScript
- ApexCharts

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature-name`
3. Make your changes and commit them: `git commit -m "Add feature-name"`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request.

Please ensure that your code follows the project's coding style and conventions. Also, provide a clear description of your changes and the problem they solve.

## License

<!-- This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details. -->

