import requests

print("=" * 60)
print("Testing Motivational Quotes Microservice")
print("=" * 60)

# Test 1: Basic report (all data)
print("\nTest 1.0: Retrieve one quote")
response = requests.get(f"http://localhost:1400/quotes/1")
print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    result = response.json()
    print(f"Result: ${result}")
    print(f"Expected one quote")
    print("✓ PASS" if len(result) == 1 else "FAIL")

else:
    print(f"✗ FAIL - Error: {response.text}")

print("\nTest 2: Retrieve three quotes")
response = requests.get(f"http://localhost:1400/quotes/3")
print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    result = response.json()
    print(f"Result: ${result}")
    print(f"Expected three quotes")
    print("✓ PASS" if len(result) == 3 else "FAIL")
else:
    print(f"✗ FAIL - Error: {response.text}")

print("\nTest 3: Unique quotes")
#current number of quotes in file: 17
response = requests.get(f"http://localhost:1400/quotes/17")
print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    result = response.json()
    print(f"Result: ${result}")
    print(f"Expected seventeen unique quotes")
    unique_quotes = set()
    for quote in result:
        unique_quotes.add(quote)
    print("✓ PASS" if len(result) == len(unique_quotes) else "FAIL")
else:
    print(f"✗ FAIL - Error: {response.text}")
