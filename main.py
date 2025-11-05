import threading
import requests
import json
from flask import Flask, request

app = Flask(__name__)

part2_value = None  

@app.route("/", methods=["POST"])
def receive_part2():
    global part2_value
    data = request.get_data(as_text=True)
    print("✅ Received Part 2:", data)

    try:
        data_json = json.loads(data)
        part2_value = data_json.get("part2")
    except Exception:
        part2_value = data

    return "OK", 200


def run_flask():
    app.run(port=8000)


def main():
    threading.Thread(target=run_flask, daemon=True).start()

    API_URL = "https://test.icorp.uz/interview.php"
    WEBHOOK_URL = "https://peachiest-rubin-aurorally.ngrok-free.dev"  
    MSG = "Hello, this is a test message!"

    print(">>> Sending POST request ....")
    response = requests.post(API_URL, json={"msg": MSG, "url": WEBHOOK_URL})

    try:
        data = response.json()
        part1 = data.get("part1")
    except Exception:
        part1 = response.text.strip()

    print("Part 1:", part1)

    # 2-qadam: 2-qismni kutish
    print("\n⌛ Waiting for Part 2 to arrive via webhook...")
    global part2_value
    while part2_value is None:
        pass  

    part2 = part2_value
    print("Part 2:", part2)

    code = f"{part1}{part2}"
    print("\nCombined Code:", code)

    print("\n>>> Sending GET request...")
    final_resp = requests.get(API_URL, params={"code": code})

    print("\n✅ Final Response:")
    print(final_resp.text)
    print(f"Full url : {API_URL}?code={code}")

if __name__ == "__main__":
    main()
