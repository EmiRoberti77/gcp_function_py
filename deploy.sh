gcloud functions deploy run_report \
  --runtime python311 \
  --trigger-http \
  --allow-unauthenticated \
  --region=us-central1
