FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y cron

# Copy the backend code and model file into the container
COPY ./backend /app/backend
COPY ./models/xgboost_model.joblib /app/models/xgboost_model.joblib
COPY ./backend_preprocessing.py /app/backend_preprocessing.py
COPY ./order_class.py /app/order_class.py
COPY ./positions.py /app/positions.py
COPY ./data/btc_15m_data_2018_to_2025.csv /app/data/btc_15m_data_2018_to_2025.csv

COPY crontab.txt /etc/cron.d/data_updater_cron
RUN chmod 0644 /etc/cron.d/data_updater_cron
RUN crontab /etc/cron.d/data_updater_cron

RUN mkdir -p /app/logs
# Expose the port
EXPOSE 8000

# Copy the start script
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

# Use the start script as the CMD
CMD ["/app/start.sh"]