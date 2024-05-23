import os
import pinecone

from dotenv                                  import load_dotenv, find_dotenv
from langchain.llms                          import HuggingFaceHub
from langchain.prompts                       import PromptTemplate
from langchain.embeddings                    import HuggingFaceEmbeddings
from langchain.vectorstores                  import Pinecone
from langchain.text_splitter                 import CharacterTextSplitter
from langchain.schema.runnable               import RunnablePassthrough
from langchain.schema.output_parser          import StrOutputParser
from langchain.document_loaders.csv_loader   import CSVLoader
load_dotenv(find_dotenv())

class ChatBot_Manettas():
    def __init__(self):
        load_dotenv()
        loader        = CSVLoader(file_path='./data/manettas_bot.csv')
        documents     = loader.load()

        #split
        text_splitter = CharacterTextSplitter(chunk_size=1500,
                                              chunk_overlap=5)
        
        self.docs     = text_splitter.split_documents(documents)

        # Langchain Embeddings, Vector Representation on some text
        embeddings    = HuggingFaceEmbeddings()

        # Langchain Retrieval
        pinecone.init(
            api_key=os.getenv('PINECONE_API_KEY'),
            environment='gcp-starter'
        )

        # nama dari indexes pada database pinecone (cuman dibolehin 1 index karena gratis)
        index_name    = "manettas_chatbot"

        # cek apakah index sudah ada atau belum, sehingga ketika dijalankan berulang kali itu amanlah
        if index_name not in pinecone.list_indexes():
            pinecone.create_index(name=index_name,
                                  metric="cosine", #cosine similliarity
                                  dimension=768)
            
            self.docsearch = Pinecone.from_documents(self.docs,
                                                     embeddings,
                                                     index_name=index_name)

        else:
            self.docsearch = Pinecone.from_existing_index(index_name,
                                                          embeddings)

        repo_id = "HuggingFaceH4/zephyr-7b-beta"
        self.llm = HuggingFaceHub(
            repo_id=repo_id,model_kwargs={"temperature": 0.8,
                                           "top_p": 0.8,
                                           "top_k": 100,
                                           "max_new_tokens": 500}, # max token yang bisa di generate oleh bot
                                           huggingfacehub_api_token=os.getenv('HUGGINGFACE_API_KEY')
        )

        # Langchain prompting
        template = """
        You are an excited asisstant for Manettas Website that sells mainly seafood product and other related seafood product for an online seafood marketplace in Australia. Use the folllowing product information to answer our customer questions.
        If you don't know the answer, just say you don't know.
        Provide a detailed and comprehensive answer, covering all aspects relevant to the question. Aim for at least 4-5 sentences, and elaborate as much as possible within the given context.

        Context: {context}
        Question: {question}
        Answer:
        """

        # Prompt Template untuk bot dengan input variabel
        self.prompt = PromptTemplate(template=template, input_variables=["context", "question"])

        # Langchain Output Parser untuk mengambil jawaban dari output model, karena output model bisa jadi banyak sehingga perlu di filter 'Answer:'
        class MyOutputParser(StrOutputParser):
            def parse(self, text):
                answer_start = text.find("Answer:") + len("Answer:")
                return text[answer_start:].strip()

        # Langchain Chains, RAG = Retrieve, Answer, Generate
        self.rag_chain = (
            {"context": self.docsearch.as_retriever(), "question": RunnablePassthrough()}
            | self.prompt
            | self.llm
            | MyOutputParser()
        )