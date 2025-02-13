types = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip",
    "mp4": "video/mp4",
    "csv": "text/csv",
}

s = input("File name: ").strip().lower().split(".")[-1]
print(types.get(s, "application/octet-stream"))
