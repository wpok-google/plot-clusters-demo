# Instructions

## Run app locally
1. Clone/upload this folder (`plot-clusters-demo`) to Cloud Shell, or use Cloud Shell Editor. The important files are:

- `app.py`
- `requirements.txt`
- `data/clusters.csv`

2. Setup the Python virtual environment:

In Cloud Shell, execute the following commands:
```
python3 -m venv plot-clusters-demo-env
source plot-clusters-demo-env/bin/activate
pip install -r requirements.txt
```

3. Setup environment variables:

In Cloud Shell, execute the following commands:
```
export GCP_PROJECT=<PROJECT_ID>
export GCP_REGION='us-central1'
```

4. To run the application locally, execute the following command:

In Cloud Shell, execute the following command:
```
streamlit run app.py \
  --browser.serverAddress=localhost \
  --server.enableCORS=false \
  --server.enableXsrfProtection=false \
  --server.port 8080
```

5. View the output at http://localhost:8080
