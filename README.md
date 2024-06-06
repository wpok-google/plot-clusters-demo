# Instructions

## Run app locally
1. Clone/upload this folder (`plot-clusters-demo`) to Cloud Shell, or use Cloud Shell Editor. The important files are:

- `app.py`
- `requirements.txt`
- `Dockerfile`
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


## Build/deploy the app to Cloud Run

1. Setup environment variables:

    In Cloud Shell, execute the following commands:

    ```bash
    export GCP_PROJECT=<PROJECT_ID>
    export GCP_REGION='us-central1'
    ```

2. Build the Docker image for the application and push it to Artifact Registry

    In Cloud Shell, execute the following commands:

    ```bash
    export AR_REPO='plot-clusters-repo'  # Dashes, no underscores
    export SERVICE_NAME='plot-clusters-demo' # Dashes, no underscores

    #make sure you are in the active directory for 'plot-clusters-demo'
    gcloud artifacts repositories create "$AR_REPO" --location="$GCP_REGION" --repository-format=Docker
    gcloud builds submit --tag "$GCP_REGION-docker.pkg.dev/$GCP_PROJECT/$AR_REPO/$SERVICE_NAME"
    ```
3.  Deploy the service in Cloud Run with the image that we
    had built and had pushed to the Artifact Registry in the previous step:

    In Cloud Shell, execute the following command:

    ```bash
    gcloud run deploy "$SERVICE_NAME" \
      --port=8080 \
      --image="$GCP_REGION-docker.pkg.dev/$GCP_PROJECT/$AR_REPO/$SERVICE_NAME" \
      --allow-unauthenticated \
      --region=$GCP_REGION \
      --platform=managed  \
      --project=$GCP_PROJECT \
      --set-env-vars=GCP_PROJECT=$GCP_PROJECT,GCP_REGION=$GCP_REGION

4. View the output at https://plot-clusters-demo-qrscbr27oa-uc.a.run.app/
      