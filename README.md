# My Presentation and Code from the Merge conference

# Rag King
Rag King is a Python application designed to analyze and extract meaningful insights from complex datasets. It uses a variety of libraries including os, vectors, dataset, together, and PyPDF2 to perform its operations.

# Features
- Extracts text from PDF files
- Creates a knowledge base from a directory of flat text files
- Allows querying and conversation with the current database
- Uses the Together API for chat completions

## Installation
Before running the script, make sure to install the necessary Python libraries. You can do this by:

install via the requirements.txt file

or directly via
`pip install PyPDF2 together tiktoken numpy SentenceTransfomer`

Need to download the huggingface repo for nomic-embed-text-v1.5 here https://huggingface.co/nomic-ai/nomic-embed-text-v1.5. this is the embedding model to use.

Need to make an account and provide a together.ai token. https://www.together.ai 

# Usage
To use the application, run the rag_king.py script. You will be presented with a menu of options:

```
Please select one of the following options:
1. Update a knowledge base # This adds more data to an existing dataset
2. Create a new knowledge base # This creates a dataset
3. Query/converse with current database
-quit to exit the program
```

Choose an option by entering its corresponding number. If you choose to create a new knowledge base, you will be asked to enter the path to a directory of flat text files. These files will be processed and added to the knowledge base.

If you choose to query the current database, you will be able to enter a query and the application will return the most relevant results from the knowledge base.

The code will create a json file called knoweldge_base.json. This is where all input chunks and vectors go.
