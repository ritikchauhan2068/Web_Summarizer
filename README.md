##  🌐 Web Summarizer with LangChain

A powerful and easy-to-use **Web Article Summarizer** built using **LangChain**, **LLMs**, and **BeautifulSoup**.
This tool takes any webpage URL, extracts readable content, splits it intelligently, and generates a clean and concise summary using advanced language models.

---

## 📖 About the Project

The **Web Summarizer** helps users quickly understand long articles, blogs, or documentation pages.
It is built using **LangChain**, allowing easy integration with HuggingFace, OpenAI, or any other LLM provider.

Whether you're doing research, reading news, or processing large amounts of content — this tool delivers fast, accurate summaries.

---

## ⭐ Features

* 🔗 Fetch and extract content from **any webpage URL**
* 🧹 Clean HTML into readable text using **BeautifulSoup**
* ✂️ Split text using **RecursiveCharacterTextSplitter**
* 🧠 Summarize using any LangChain-supported LLM
* 🧱 Modular and easily extendable architecture
* 🌐 Works with OpenAI, HuggingFace, or custom models
* ⚡ Fast, efficient, and reliable

---

## 📁 Project Structure

```
web-summarizer/
│── app.py                  # Main script for summarization
│── requirements.txt        # Project dependencies
│── README.md               # Documentation
│── .env                    # API keys (ignored by Git)
```

---

## 🛠 Tech Stack

* **Python 3.9+**
* **LangChain**
* **HuggingFace / OpenAI / Any LLM provider**
* **BeautifulSoup4**
* **Requests**
* **dotenv**

---

## 🔧 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/web-summarizer.git
cd web-summarizer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the root folder:

```
HF_API_KEY=your_huggingface_api_key
OPENAI_API_KEY=your_openai_api_key  # optional
```

These keys allow access to LLM APIs.

---

## ⚙️ How It Works

1. **User enters a webpage URL**
2. The app fetches HTML using `requests`
3. BeautifulSoup extracts readable text
4. `RecursiveCharacterTextSplitter` breaks the content into overlapping chunks
5. Each chunk is summarized individually
6. All summaries are merged into a final clean output


---



## 🚀 Future Enhancements

* 🖥️ Add a **Streamlit UI**
* 🧠 Add multi-language summarization
* 📄 Add PDF / YouTube / Doc summarizer
* 📝 Add note-taking and export options
* 📊 Add keyword extraction + topic clustering
* 🧬 Use embedding-based long-document summarization

---

## 🤝 Contributing

Contributions are welcome!
You can open an issue or submit a pull request.

