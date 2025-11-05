# 🚀 Webhook Integration Demo (Flask + Requests)


This project demonstrates how to work with webhooks in Python using Flask and requests.
It runs a local Flask server to receive data (part2) via webhook, while sending and receiving other data (part1) from an external API.

## How it works
- The Flask server starts on port 8000 and acts as the webhook receiver.
- The program sends a POST request to:

```script
https://test.icorp.uz/interview.php
```

with the following JSON payload:
```json
{
  "msg": "Hello, this is a test message!",
  "url": "https://<your-ngrok-url>.ngrok-free.dev"
}
```

- The url value tells the remote server where to send the webhook callback.
- The remote API responds with part1.
- Later, the remote server makes a POST request back to your WEBHOOK_URL (the Flask endpoint) containing part2.
- Once both part1 and part2 are received, they are combined into a single code.
- Finally, a GET request is made with this code:

```script
https://test.icorp.uz/interview.php?code=<part1><part2>
```
- The final response is printed in the terminal.

## 🛠️ Installation

```shell
pip install flask requests
```


## Start ngrok:
Since Flask runs locally, use ngrok to expose it to the internet:

```bash
ngrok http 8000
```

Copy the generated HTTPS link (e.g. https://xxxxxx.ngrok-free.dev)
and replace it inside the script:

```python
WEBHOOK_URL = "https://xxxxxx.ngrok-free.dev"
```

## Run the Script
```python
python3 main.py
```

### Example output:

```bash
 * Serving Flask app 'main'
>>> Sending POST request ....

✅ Received Part 2: {"part2":"yyy"}

Part 1: xxx

⌛ Waiting for Part 2 to arrive via webhook...
Part 2: yyy

Combined Code: xxx+yyy

>>> Sending GET request...

✅ Final Response:
{"msg":"Hello, this is a test message!"}
Full url : https://test.icorp.uz/interview.php?code=xxxyyy

```

