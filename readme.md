# Google Cloud Function - Python HTTP API Example

This project demonstrates how to build and deploy a **Python-based HTTP Google Cloud Function**.  
It returns a JSON object with a success flag and a timestamp.

---

## Project Structure

```
gcp-function_py/
├── main.py
└── requirements.txt
```

---

## Files Description

### `main.py`

```python
import datetime
from flask import jsonify

def run_report(request):
    """HTTP Cloud Function that returns a JSON success response with a timestamp."""
    response = {
        "success": True,
        "timeStamp": datetime.datetime.utcnow().isoformat()
    }
    return jsonify(response)
```

### `requirements.txt`

```
# No external libraries required for this example
```

---

## Prerequisites

- Google Cloud CLI installed and configured
- Billing enabled on your GCP Project
- Cloud Functions API enabled

---

## Deployment Instructions

### 1. Navigate to Your Function Directory

```bash
cd gcp-function_py
```

### 2. Deploy the Function

```bash
gcloud functions deploy run_report \
  --runtime python311 \
  --trigger-http \
  --allow-unauthenticated \
  --region=us-central1
```

---

## Access Your Function

After deployment, note the **URL** provided by the command output.

Example:

```
https://us-central1-emi-dev-env-2.cloudfunctions.net/run_report
```

---

## 🧪 Example Invocation

### cURL Example

```bash
curl https://us-central1-emi-dev-env-2.cloudfunctions.net/run_report
```

### Example JSON Response

```json
{
  "success": true,
  "timeStamp": "2025-05-19T05:37:10.101800"
}
```

---

## Summary

- Python 3.11 HTTP Function
- JSON Success Response with Timestamp
- Deployed on GCP Cloud Functions
- Accessible via HTTP with cURL or browser

---

## Security Tip

For production, **remove** `--allow-unauthenticated` and configure **IAM permissions** or **API Gateway** for authentication.

## Author

`Emiliano Roberti`
