import os
from dotenv import load_dotenv
import boto3
from botocore.exceptions import BotoCoreError, ClientError

# Load environment variables from .env file
load_dotenv()

def main():
    try:
        db_name = os.getenv('dbName', 'replaceme')
        table_name = os.getenv('tableName', 'replaceme')
        profile_name = os.getenv('profile')
        rows = os.getenv('rows', '1')
        endpoint_url = os.getenv('endpointURL')

        query_string = f'SELECT * FROM "{db_name}"."{table_name}" LIMIT {rows}'

        session = boto3.Session(profile_name=profile_name) if profile_name else boto3.Session()
        client = session.client('timestream-query', region_name='eu-west-1', endpoint_url=endpoint_url)

        query_request = {
            'QueryString': query_string
        }

        query_response = client.query(**query_request)

        if 'Rows' in query_response and len(query_response['Rows']) > 0:
            for row in query_response['Rows']:
                for datum in row['Data']:
                    if 'ScalarValue' in datum:
                        print(f"{datum['ScalarValue']} ", end="")
                    else:
                        print("NULL ", end="")
                print()
        else:
            print("No rows returned.")

    except (BotoCoreError, ClientError) as e:
        print(f"AWS Timestream Query Error: {e}")
    except Exception as ex:
        print(f"Error querying Timestream: {ex}")

if __name__ == "__main__":
    main()
