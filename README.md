## Installation

```bash
pip install openai chainlit
```

## Anwendung starten

```bash
chainlit run start.py
```

## LangChain und MediaWiki-Dump installieren

```bash
pip install langchain
pip install mwparserfromhell
```

MediaWiki-Dumps enthalten viel Overhead. Wir benötigen nur den Titel und den Textinhalt.
```
from langchain_community.document_loaders import MWDumpLoader

# Pfad zu deinem XML-Dump (z.B. pages-articles.xml)
loader = MWDumpLoader(
    file_path="dein_wiki_dump.xml",
    encoding="utf-8"
)

# Lädt die Daten als Liste von "Documents"
documents = loader.load()
```
Chunking (Text in Stücke schneiden)
```
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100,
    add_start_index=True
)

chunks = text_splitter.split_documents(documents)
```
Vector Store erstellen (Indizierung)
```
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# Nutzt ein lokales Modell für Embeddings (kostet nichts)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Datenbank lokal speichern
vector_db = Chroma.from_documents(
    documents=chunks, 
    embedding=embeddings, 
    persist_directory="./wiki_db"
)
```
