from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma

persist_directory = "docs/docs/chroma"
ROLE_URLS = {
    "it": ["https://csc.fi/en/trainings/training-calendar/training-archive/"],
    "hr": ["https://csc.fi/en/careers/"],
    "finance": [],
    "all": [],  # general policies everyone needs
}

docs = []
for role, urls in ROLE_URLS.items():
    if not urls:
        continue
    pages = WebBaseLoader(urls).load()
    for d in pages:
        d.metadata["dept"] = role  # critical for role filtering
        docs.append(d)

splits = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=1000, chunk_overlap=150
).split_documents(docs)

emb = OpenAIEmbeddings()
Chroma.from_documents(
    splits, emb, persist_directory=persist_directory, collection_name="onboarding"
).persist()
