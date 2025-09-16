# Tamil Nadu Flood Analysis Agent 🌊

This project is an **AI-powered flood analysis pipeline** built with  
[LangChain](https://www.langchain.com/), [Ollama](https://ollama.ai/), and [Chroma](https://www.trychroma.com/).  

It loads a dataset of **Tamil Nadu flood events (2024)**, embeds the data into a vector database, and allows you to ask natural language questions about flood patterns, rainfall, affected populations, and damages.

---

## 🚀 Features
- Loads structured flood dataset (`tamilnadu_floods_2024.csv`)
- Embeds events using **Ollama Embeddings**
- Stores/retrieves knowledge with **Chroma vector DB**
- Uses **LLaMA 3.2 (via Ollama)** for answering questions
- Interactive CLI (`main.py`) where you can ask questions like:
  - *Which districts had flood levels above 3 meters?*
  - *Which district reported the highest damages?*
  - *How many people were affected in Chennai floods?*

---

## 📂 Project Structure
```
ai-agent/
│
├── main.py                     # Entry point for Q&A
├── vector.py                   # Builds Chroma vector DB from CSV
├── tamilnadu_floods_2024.csv   # Flood dataset (sample)
└── README.md                   # Documentation
```

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/ai-agent.git
cd ai-agent
```

### 2. Install dependencies
Make sure you have Python 3.9+ and pip installed.

```bash
pip install langchain langchain-ollama langchain-chroma pandas
```

### 3. Install & run Ollama
Follow [Ollama installation guide](https://ollama.ai/download).  
Make sure you pull the required models:

```bash
ollama pull llama3.2
ollama pull mxbai-embed-large
```

---

## ▶️ Usage

### Build the vector store
The first time you run, `vector.py` will embed the flood dataset into Chroma.

### Start interactive Q&A
```bash
python main.py
```

You’ll be prompted to type a question:
```
Ask question or type 0 to quit > Which districts had flood levels above 3m?
```

---

## 📊 Dataset

`tamilnadu_floods_2024.csv` is a **synthetic dataset** with:
- District  
- Date  
- Flood Level (m)  
- Rainfall (mm)  
- Affected Population  
- Damages (Crores INR)  

Example row:

```
District,Date,Flood_Level_m,Rainfall_mm,Affected_Population,Damages_Crores_INR
Chennai,2024-11-12,2.5,310,120000,850
```

---

## 🔮 Future Improvements
- Add visualization dashboards (Matplotlib / Streamlit)
- Support multi-year flood data
- Deploy as a web app for interactive queries

---

## 📝 License
MIT License. Free to use, modify, and distribute.
