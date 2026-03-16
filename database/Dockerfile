# Use Python 3.14 slim image
FROM python:3.14-slim

# Install uv
RUN pip install uv

# Set working directory
WORKDIR /app

# Copy project files
COPY pyproject.toml .
COPY main.py .

# Install dependencies using uv
RUN uv pip install --system -e .

# Run the script
CMD ["python", "main.py"]