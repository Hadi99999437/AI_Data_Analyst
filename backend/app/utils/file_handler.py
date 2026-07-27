import os
import uuid
from fastapi import UploadFile

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


async def save_upload_file(file: UploadFile):

    extension = file.filename.split(".")[-1]

    stored_name = f"{uuid.uuid4()}.{extension}"

    path = os.path.join(
        UPLOAD_DIR,
        stored_name,
    )

    with open(path, "wb") as buffer:
        buffer.write(await file.read())

    return stored_name, path