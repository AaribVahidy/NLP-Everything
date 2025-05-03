import streamlit as st
from vsm_engine import process_query
import os

# Set page configuration
st.set_page_config(page_title="Vector Space Model IR", page_icon="🔍", layout="centered")

# App title and description
st.title("🔍 Information Retrieval using VSM")
st.markdown("""
Welcome to the Vector Space Model-based Information Retrieval system! 👑
Enter a query below, and find the most relevant documents in the dataset.
""")

# Text input for query
query = st.text_input("Enter your query here:", placeholder="e.g., ensemble")

if query:
    # Process the query
    results = process_query(query)

    # Sort results by document number (doc_id)
    if results:
        sorted_results = sorted(results, key=lambda x: x[0])  # Sort by document ID (first element)
        
        st.subheader(f"📄 Top Relevant Documents for '{query}':")
        for doc_id, score in sorted_results:
            st.write(f"**Doc {doc_id}** — Score: `{score:.4f}`")
    else:
        st.warning("No relevant documents found. Try rephrasing the query.")
else:
    st.info("Please enter a query to search for relevant documents.")

# Optional: Display gold queries if file exists
gold_file = "Gold-Query-VSM.txt"

if os.path.exists(gold_file):
    with st.expander("📚 Run Golden Queries"):
        try:
            with open(gold_file, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            current_query = None
            current_relevant_docs = []
            queries = []

            for line in lines:
                line = line.strip()
                if not line:
                    continue

                if ')' in line:
                    if current_query:
                        queries.append({
                            "query": current_query,
                            "relevant_docs": current_relevant_docs
                        })
                    current_query = line
                    current_relevant_docs = []
                else:
                    doc_ids = [int(x.strip()) for x in line.split(',') if x.strip().isdigit()]
                    current_relevant_docs.extend(doc_ids)

            if current_query:
                queries.append({
                    "query": current_query,
                    "relevant_docs": current_relevant_docs
                })

            # Dropdown for golden query selection
            query_choices = [q["query"] for q in queries]
            selected_query = st.selectbox("Choose a golden query to test:", query_choices)

            if st.button("Run Golden Query"):
                golden_result = process_query(selected_query)
                
                # Sort results for the golden query by document number
                sorted_golden_result = sorted(golden_result, key=lambda x: x[0])  # Sort by document ID (first element)
                
                st.subheader(f"Results for: '{selected_query}'")
                for doc_id, score in sorted_golden_result:
                    st.write(f"**Doc {doc_id}** — Score: `{score:.4f}`")
        
        except Exception as e:
            st.error(f"Error loading golden queries: {e}")
else:
    st.warning("Gold-Query-VSM.txt file not found.")
