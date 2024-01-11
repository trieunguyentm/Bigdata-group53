from vnstock import *
from kafka import KafkaProducer
import json
import time
from get_list_companies import get_list_companies

# Initialize a Kafka producer with multiple brokers
producer = KafkaProducer(bootstrap_servers=['localhost:9092', 'localhost:9093', 'localhost:9094'],
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))


def fetch_and_send_data(ticker):
    try:
        # Fetch real-time data
        df_intraday = stock_intraday_data(
            symbol=ticker, page_size=1000, investor_segment=False)

        # Check and remove invalid data
        if df_intraday['ticker'].isnull().any():
            print(f"Invalid data detected for ticker {ticker}: skipping...")
            return

        # Iterate over DataFrame rows and send each row as a separate JSON object
        for index, row in df_intraday.iterrows():
            data = row.to_json()
            # Print data to Console before sending
            print(f"Data to be sent for ticker {ticker}: {data}")
            producer.send('test_topic', value=data)
            print(f"Data sent to Kafka for ticker {ticker}")
    except Exception as e:
        print(f"Error when getting data for ticker {ticker}: {e}")


def main():
    # Assuming get_list_companies is a function that returns a list of stock tickers
    tickers = get_list_companies()
    while True:
        for ticker in tickers:
            fetch_and_send_data(ticker)
            # Sleep between requests to avoid hitting API rate limits
            time.sleep(0.5)
        # Sleep after processing all tickers
        n = input("Tạm dừng fetchdata")
        time.sleep(60)


if __name__ == "__main__":
    main()
