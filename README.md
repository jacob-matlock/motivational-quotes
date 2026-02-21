# Motivational Quotes Microservice

A Flask-based microservice for randomly generating motivational quotes 

## Features

- Randomized motivational quotes
- Unique quotes until collection has been used
- RESTful API interface


## Requirements

```bash
pip install flask
```

## Quick Start

1. **Start the service:**
   ```bash
   python main.py
   ```
   Service runs on `http://localhost:1400`

2. **Run tests:**
   ```bash
   python test.py
   ```

## API Usage

**Endpoint:** `GET /quotes/<num_quotes>`

**Request:**
```
	requests.get(f"http://localhost:1400/quotes/1")
```

**Response:**
```
{["The elevator to success is out of order. You’ll have to use the stairs, one step at a time." Joe Girard]}

```


## Files

- `main.py` - Flask API server
- `quotes.txt` - Collection of motivational quotes
- `test.py` - Test suite with examples

## Error Codes

- `200` - Success
