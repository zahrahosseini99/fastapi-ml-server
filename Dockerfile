FROM continuumio/miniconda3

WORKDIR /app

COPY . .

RUN conda env create -f environment.yml

SHELL ["conda", "run", "-n", "fastapi-ml", "/bin/bash", "-c"]

CMD ["conda", "run", "--no-capture-output", "-n", "fastapi-ml", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
