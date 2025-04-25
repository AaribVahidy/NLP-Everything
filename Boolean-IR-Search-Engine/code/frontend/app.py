import streamlit as st
from search_engine import boolean_query, proximity_query

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #f5f5f5;
        }
        .main {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }
        .stTextInput, .stButton>button {
            font-size: 16px;
            padding: 10px;
            border-radius: 5px;
        }
        .stMarkdown {
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

# Streamlit Layout
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🔍 Boolean Information Retrieval System by Aarib Ahmed Vahidy 22K-4004</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>This system allows you to search a collection of computer science abstracts using Boolean Queries.</p>", unsafe_allow_html=True)

# Sidebar with styling
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/1041/1041916.png", width=120) #sidebar logo

st.sidebar.markdown("<h2 style='color: #4CAF50;'>Query Guidelines 📝</h2>", unsafe_allow_html=True)
st.sidebar.markdown("""
- **Use Boolean operators** (AND, OR, NOT) to search.  
  **Example:** `image AND restoration`
- **Use Proximity Search** (`/k`) to find words within k distance.  
  **Example:** `feature track /5`
- **Query can contain up to 3 terms.**
""")

# User Input Section
st.markdown("<h3>Enter Your Query Below:</h3>", unsafe_allow_html=True)
query = st.text_input("Enter your search query:")

# Processing the query when submitted
if st.button("Search 🔎"):
    query = query.strip()
    
    if not query:
        st.warning("⚠️ Please enter a valid query.")
    else:
        if "/" in query:
            try:
                parts = query.split()
                term1 = parts[0]
                term2 = parts[1]
                k = int(parts[2][1:])  # Extracting k from "/k"

                results = proximity_query(term1, term2, k)
                query_type = "Proximity Search"
            except Exception:
                st.error("❌ Invalid proximity query format. Use: `term1 term2 /k` (Example: feature track /5)")
                results = []
        else:
            query_parts = query.split()
            if len(query_parts) == 1:
                term1 = query_parts[0]
                results = boolean_query(term1)
                query_type = "Single-Term Search"
            elif len(query_parts) == 3:
                term1, operator1, term2 = query_parts
                results = boolean_query(term1, operator1, term2)
                query_type = "Two-Term Boolean Search"
            elif len(query_parts) == 5:
                term1, operator1, term2, operator2, term3 = query_parts
                results = boolean_query(term1, operator1, term2, operator2, term3)
                query_type = "Three-Term Boolean Search"
            else:
                st.error("❌ Invalid Boolean query format. Use up to three terms with AND, OR, NOT.")
                results = []

        # Displaying results
        st.markdown(f"<h3>🔎 {query_type} Results:</h3>", unsafe_allow_html=True)
        if results:
            st.success(f"✅ Documents matching query `{query}`:")
            st.write(results)
        else:
            st.warning("⚠️ No matching documents found.")
