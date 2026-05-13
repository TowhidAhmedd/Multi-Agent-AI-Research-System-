# Multi-Agent-AI-Research-System-


# ML Research Assistant

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.38.0-red.svg)](https://streamlit.io/)
[![Weaviate](https://img.shields.io/badge/Weaviate-4.6.3-green.svg)](https://weaviate.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Retrieval-Augmented Generation (RAG) based ML Research Assistant that enables semantic search and question-answering over arXiv papers using Weaviate vector database and advanced NLP techniques.

## Features

- **Data Ingestion**: Load and process scientific papers from arXiv dataset
- **Advanced Chunking**: Multiple chunking strategies (fixed-size, sentence-based, semantic)
- **Vector Embeddings**: Sentence-transformer based embeddings for semantic search
- **Weaviate Integration**: Cloud-hosted vector database for scalable retrieval
- **RAG Pipeline**: End-to-end retrieval and generation with LLM support (OpenAI, Groq)
- **Reranking**: Cross-encoder based reranking for improved retrieval quality
- **Evaluation Metrics**: Comprehensive RAG evaluation with 5 key metrics
- **Streamlit UI**: Interactive web interface for research queries
- **Deployment Ready**: Scripts for AWS EC2 deployment

## Architecture

```
Data Source (arXiv) → Chunking → Embeddings → Weaviate Index → RAG Pipeline → UI
```

### Components

- **Data Layer**: `app/data/` - ArXiv paper loading and preprocessing
- **Ingestion Layer**: `app/ingestion/` - Chunking, embeddings, and Weaviate indexing
- **RAG Layer**: `app/rag/` - Retrieval, reranking, evaluation, and LLM integration
- **UI Layer**: `app/ui/` - Streamlit-based web interface
- **Scripts**: `scripts/` - Index building and maintenance utilities
- **Deployment**: `deploy/` - AWS EC2 deployment scripts

## Installation

### Prerequisites

- Python 3.10+
- Weaviate Cloud account (for vector database)
- OpenAI API key (for LLM generation)
- Groq API key (optional, for alternative LLM)

### Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd ml-research-assistant
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   Create a `.env` file in the project root:
   ```env
   WEAVIATE_URL=your-weaviate-cloud-url
   WEAVIATE_API_KEY=your-weaviate-api-key
   OPENAI_API_KEY=your-openai-api-key
   GROQ_API_KEY=your-groq-api-key  # Optional
   ```

## Usage

### Build the Index

First, build the Weaviate index with arXiv papers:

```bash
python scripts/build_index.py
```

This will:
- Load papers from the arXiv dataset
- Apply chunking strategy (configurable in `app/config.py`)
- Generate embeddings
- Index chunks in Weaviate

### Run the Application

Start the Streamlit web interface:

```bash
streamlit run app/ui/streamlit_app.py
```

The app will be available at `http://localhost:8501`

### Features in UI

- **Semantic Search**: Query scientific papers with natural language
- **RAG Evaluation**: View retrieval metrics and performance
- **Reranking Toggle**: Enable/disable cross-encoder reranking
- **Chunking Configuration**: Adjust chunking parameters

## Configuration

Key configuration options in `app/config.py`:

- **Dataset**: HuggingFace dataset name and config
- **Chunking**: Size, overlap, and strategy
- **Embeddings**: Model selection (via sentence-transformers)
- **LLM**: Provider selection (OpenAI/Groq)

## Deployment

### AWS EC2 Deployment

Follow the detailed guide in [DEPLOYMENT.md](DEPLOYMENT.md) for deploying to AWS EC2.

**Quick steps**:
1. Launch Ubuntu EC2 instance
2. Configure security groups (SSH + port 8501)
3. Upload project files using SCP
4. Run setup script: `bash deploy/setup_ec2.sh`
5. Start application: `bash deploy/start_app.sh`

### Local Deployment

For local deployment with Docker (if configured):

```bash
# Build and run (assuming Dockerfile exists)
docker build -t ml-research-assistant .
docker run -p 8501:8501 ml-research-assistant
```

## Development

### Project Structure

```
ml-research-assistant/
├── app/
│   ├── config.py              # Configuration settings
│   ├── data/
│   │   └── load_arxiv.py      # ArXiv data loading
│   ├── ingestion/
│   │   ├── chunking.py        # Document chunking strategies
│   │   ├── embeddings.py      # Embedding generation
│   │   └── index_weaviate.py  # Weaviate indexing
│   ├── rag/
│   │   ├── pipeline.py        # Main RAG pipeline
│   │   ├── retriever.py       # Vector retrieval
│   │   ├── reranker.py        # Reranking logic
│   │   ├── evaluation.py      # RAG evaluation metrics
│   │   └── llm_client.py      # LLM integration
│   └── ui/
│       └── streamlit_app.py   # Web interface
├── scripts/
│   └── build_index.py         # Index building script
├── deploy/
│   ├── setup_ec2.sh           # EC2 setup script
│   ├── start_app.sh           # Application startup
│   └── copy_to_ec2.ps1        # Windows SCP script
├── pyproject.toml             # Project metadata
├── requirements.txt           # Python dependencies
├── DEPLOYMENT.md              # Deployment guide
└── README.md                  # This file
```

### Adding New Features

1. **Data Sources**: Extend `app/data/` for new datasets
2. **Chunking Strategies**: Add methods in `app/ingestion/chunking.py`
3. **LLM Providers**: Implement in `app/rag/llm_client.py`
4. **UI Components**: Modify `app/ui/streamlit_app.py`

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make changes and test thoroughly
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [arXiv](https://arxiv.org/) for the scientific paper dataset
- [Weaviate](https://weaviate.io/) for vector database
- [Hugging Face](https://huggingface.co/) for datasets and models
- [OpenAI](https://openai.com/) and [Groq](https://groq.com/) for LLM APIs





