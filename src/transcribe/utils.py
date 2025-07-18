import tempfile
import uuid
import os
import requests

def download_temp_audio(url: str) -> str:
    temp_dir = tempfile.gettempdir()
    filename = os.path.join(temp_dir, f"{uuid.uuid4()}.mp3")

    response = requests.get(url, verify=False)
    response.raise_for_status()

    with open(filename, "wb") as f:
        f.write(response.content)

    return filename
