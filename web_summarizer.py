import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()
def setup_huggingface_model():
    """Setup Hugging Face model for summarization."""
    return HuggingFaceEndpoint(
        repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
        task="text-generation",
        temperature=0.3,
        max_new_tokens=1024,
    )

def load_document(url):
    """Load document from the specified URL."""
    try:
        loader = WebBaseLoader(url)
        return loader.load()
    except Exception as e:
        st.error(f"Error loading document: {str(e)}")
        return None

def generate_summary(text, model):
    """Generate summary using the model."""
    prompt_template = PromptTemplate(
        template="""You are a professional summarizer. Create a detailed and clear summary of the text below:

{text}

Detailed Summary:""",
        input_variables=["text"],
    )
    
    prompt = prompt_template.format(text=text)
    return model.invoke(prompt)

def main():
    # Page configuration
    st.set_page_config(
        page_title="Document Summarizer",
        page_icon="🧠",
        layout="wide"
    )
    
    # Title and description
    st.title("🧠 Document Summarizer")
    st.markdown("Enter a URL to summarize web content using AI")
    
    # Sidebar for settings
    with st.sidebar:
        st.header("ℹ️ About")
        st.info(
            "This app uses Mixtral-8x7B to generate summaries of web documents. "
            "Simply paste a URL and click 'Summarize'."
        )
        st.markdown("---")
        st.markdown("**Model:** Mixtral-8x7B-Instruct")
        st.markdown("**Temperature:** 0.3")
        st.markdown("**Max tokens:** 1024")
    
    # Main input area
    url = st.text_input(
        "Enter URL:",
        placeholder="https://example.com/article",
        help="Paste the URL of the document you want to summarize"
    )
    
    col1, col2 = st.columns([1, 5])
    with col1:
        summarize_button = st.button("🚀 Summarize", type="primary")
    with col2:
        if url:
            st.caption(f"Ready to summarize: {url}")
    
    # Process when button is clicked
    if summarize_button:
        if not url:
            st.warning("⚠️ Please enter a URL first!")
        else:
            with st.spinner("Loading document..."):
                docs = load_document(url)
            
            if docs:
                text = docs[0].page_content
                
                # Display original text in an expander
                with st.expander("📄 View Original Text"):
                    st.text_area(
                        "Document Content",
                        text,
                        height=300,
                        disabled=True
                    )
                
                # Generate summary
                with st.spinner("Generating summary... This may take a moment."):
                    try:
                        model = setup_huggingface_model()
                        summary = generate_summary(text, model)
                        
                        # Display summary
                        st.success("✅ Summary Generated!")
                        st.markdown("### 🧠 Summary:")
                        st.markdown(summary)
                        
                        # Download button
                        st.download_button(
                            label="📥 Download Summary",
                            data=summary,
                            file_name="summary.txt",
                            mime="text/plain"
                        )
                        
                    except Exception as e:
                        st.error(f"Error generating summary: {str(e)}")

if __name__ == "__main__":
    main()
