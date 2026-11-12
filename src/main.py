from fastapi import FastAPI

app = FastAPI(
    title="Semantic GraphRAG Engine",
    description="Knowledge Graph and Retrieval Augmented Generation API",
    version="0.1.0",
)


@app.get("/")
def home():
    return {
        "message": "Semantic GraphRAG Engine is running!",
        "status": "success",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}
