import requests
import json

class OllamaAPI:
    def __init__(self, api_url="http://localhost:11434/api/generate"):
        self.api_url = api_url

    def chat_with_ollama(self, prompt, model="qwen2:0.5b"):
        try:
            response = requests.post(
                self.api_url,
                json={"model": model, "prompt": prompt},
                stream=True  # Enable streaming
            )
            if response.status_code == 200:
                messages = []
                for line in response.iter_lines():
                    if line:
                        try:
                            json_line = line.decode('utf-8')
                            data = json.loads(json_line)
                            messages.append(data.get("response", ""))
                            if data.get("done", False):
                                break  # Stop when done is True
                        except json.JSONDecodeError:
                            continue  # Skip lines that are not valid JSON
                return "".join(messages)  # Return the concatenated response
            else:
                return f"Error: {response.status_code} - {response.text}"
        except Exception as e:
            return f"Error: {str(e)}"
