FROM python:3.12-alpine

RUN apk add --no-cache gcc musl-dev linux-headers

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY . .

# Run the app on port 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]