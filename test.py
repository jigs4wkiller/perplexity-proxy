#!/usr/bin/env python3
import requests
response = requests.get("http://localhost:8787")
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")
