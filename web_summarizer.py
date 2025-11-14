import argparse
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from langchain_huggingface import HuggingFaceEndpoint


def setup_argparse():
    """Setup argparse to parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Summarize a document from a given URL."
    )
    parser.add_argument(
        "-u", "--url", required=True, help="URL of the document to summarize"
    )
    return parser.parse_args()


def load_document(url):
    """Load document from the specified URL."""
    loader = WebBaseLoader(url)
    return loader.load()


def setup_huggingface_model():
    """Setup Hugging Face model for summarization."""
    return HuggingFaceEndpoint(
        repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",  # or any HF model you prefer
        task="text-generation",
        temperature=0.3,
        max_new_tokens=1024,
    )


def main():
    args = setup_argparse()
    docs = load_document(args.url)
    text = docs[0].page_content if docs else "No content found."

    model = setup_huggingface_model()

    prompt_template = PromptTemplate(
        template="""You are a professional summarizer. Create a detailed and clear summary of the text below:

{text}

Detailed Summary:""",
        input_variables=["text"],
    )

    prompt = prompt_template.format(text=text)

    summary = model.invoke(prompt)
    print("\n🧠 SUMMARY:\n")
    print(summary)


if __name__ == "__main__":
    main()
