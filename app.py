import streamlit as st
import requests

# designs the web interface
st.title("AI Paper Finder")
st.write("Find the most relevant scientific articles on any topic in Semantic Scholar.")

# creates a text box for user input
query = st.text_input("What topic do you want to research?", "Machine Learning")

# creates a button to trigger the search
if st.button("Search Papers"):
    with st.spinner("Searching the scientific database..."):
        
        # calls the Semantic Scholar API passing the input (query), requesting 5 results (limit)
        # and specifies the fields we want (title, authors, abstract, url)
        url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=5&fields=title,authors,abstract,url"
        
        # makes the request to the internet
        response = requests.get(url)
        
        # converts the text response into a Python dictionary (JSON)
        data = response.json()
        
        # displays the data on our web page
        if "data" in data: # checks if results were found with the label "data"
            for paper in data["data"]:
                # prints the title as a subheader or "Untitled" in case there isn't title
                st.subheader(paper.get("title", "Untitled"))
                
                # extracts author names from the list
                authors = [author["name"] for author in paper.get("authors", [])]
                st.write(f"**Authors:** {', '.join(authors)}")
                
                # prints a part of the abstract
                abstract = paper.get("abstract")
                if abstract:
                    st.write(abstract[:300] + "...") # Show only the first 300 characters
                else:
                    st.write("*No abstract available.*")
                
                # makes the link clickable
                st.markdown(f"[Read full paper]({paper.get('url')})")
                
                # adds a divider between papers
                st.divider()
        else:
            st.error("No results found. Please try different keywords.")