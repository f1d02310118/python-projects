import speedtest

def bytes_to_mb(bytes):
    KB = 1024
    MB = KB * 1024
    return int(bytes / MB)

speed = speedtest.Speedtest()

print("Finding best server...")
speed.get_best_server()

print("Testing download speed...")
download_speed = speed.download()

print("Testing upload speed...")
upload_speed = speed.upload()

print("Pinging server...")
ping_result = speed.results.ping

print(f"Download speed: ({bytes_to_mb(download_speed)} MB/s)")
print(f"Upload speed: ({bytes_to_mb(upload_speed)} MB/s)")
print(f"Ping: {ping_result} ms")