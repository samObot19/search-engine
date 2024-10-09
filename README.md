# Simple Search Engine

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
  - [Indexing](#indexing)
  - [Searching](#searching)
- [Ranking Algorithm](#ranking-algorithm)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project is a simple search engine that indexes text files located in specified directories and allows users to search through these documents. The search results are ranked using the Vector Space Model, providing users with relevant information quickly and efficiently.

## Features

- **Indexing**: Automatically indexes all `.txt` files in a designated directory and its subdirectories.
- **Searching**: Users can input keywords to search through the indexed documents.
- **Ranking**: Results are ranked based on relevance using the Vector Space Model.
- **User-friendly Output**: Displays the search results clearly, showing relevant documents.

## Technologies Used

- Python
- NLTK (Natural Language Toolkit)
- Mathematical libraries (e.g., `math`, `heapq`)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/simple-search-engine.git
   cd simple-search-engine
## Installation

### Install Required Packages

Make sure you have Python installed, then run:

```bash
pip install nltk
```

## How It Works

### Indexing

The `indexing.py` script performs the following tasks:

1. **Reads Documents**: It reads all `.txt` files from the specified `corpus` directory.
2. **Tokenization and Preprocessing**:
   - Tokenizes the content of each document.
   - Converts all text to lowercase.
   - Stems the words using a custom implementation of the Porter Stemmer.
3. **Building the Inverted Index**:
   - Constructs an inverted index that maps each stemmed word to the documents in which it appears.
   - Records the frequency of occurrences of each word in each document.

### Searching

The `vectorspace_model.py` script manages the search functionality through the following steps:

1. **User Query Input**: Accepts a search query from the user and tokenizes it.
2. **Stemming the Query**: Stems the words in the query using the same Porter Stemmer.
3. **Constructing Term Frequency Representation**: Creates a term frequency representation for the query.
4. **Reading the Inverted Index**:
   - Reads the inverted index from `index_term.txt`.
   - Computes the TF-IDF scores for each document based on the terms in the query.
5. **Ranking Documents**:
   - Calculates cosine similarity to rank the documents based on their relevance to the search query.

### Ranking Algorithm

The search engine employs the Vector Space Model, which ranks documents based on two main components:

- **Term Frequency (TF)**: The number of times a term appears in a document.
- **Inverse Document Frequency (IDF)**: Measures the importance of a term across all documents.

The relevance score for each document is calculated using the formula:

\[ 
\text{Score}(D) = \text{TF}(t, D) \times \text{IDF}(t) 
\]

Where:
- \( t \) is a term in the query.
- \( D \) is a document.

This scoring helps identify the most relevant documents to the user's query.


