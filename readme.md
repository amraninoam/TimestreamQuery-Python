# Timestream Query Python Application

This is a Python application that queries an AWS Timestream database and prints the results.

## Prerequisites

- Python 3.6 or later
- AWS CLI configured with the appropriate profile
- Docker (optional, for containerized deployment)

## Setup

1. Clone the repository:

    ```sh
    git clone https://github.com/your-repo/timestream-query-python.git
    cd timestream-query-python
    ```

2. Install dependencies:

    ```sh
    pip install boto3 python-dotenv
    ```

3. Create a `.env` file in the root of the project and add the following environment variables:

    ```plaintext
    dbName=your_db_name
    tableName=your_table_name
    profile=your_aws_profile
    rows=number_of_rows
    endpointURL=your_timestream_endpoint_url
    ```

## Running the Application

To run the application:

```sh
python index.py
