s = input("File name: ").strip().lower().split(".")[-1]

types = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip",
}

type = types.get(s, "application/octet-stream")
print(f"{type}")
