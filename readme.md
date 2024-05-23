# Manettas Online Seafood Market Chatbot

![image](https://github.com/roniantoniius/Manettas-RAG-Chatbot-with-Zephyr-7B/assets/121453378/9b947343-d021-45bb-a74e-ff92573d5be3)


## Context

In today's dynamic online seafood retail landscape, businesses face challenges related to consumer preferences, accessibility, and promoting healthy eating habits. Manettas, an online marketplace in Australia offering a variety of fresh seafood products, aims to enhance customer experience by addressing these issues. Ensuring accessibility to seafood for consumers in landlocked areas and encouraging seafood consumption among children are significant concerns. To tackle these, we developed a chatbot using the Zephyr 7B β model from Hugging Face. This chatbot leverages Retrieval-Augmented Generation (RAG) through LangChain to provide real-time, detailed responses to customer inquiries about Manettas' seafood products. By offering relevant product recommendations and comprehensive information, the chatbot aims to improve the shopping experience and promote the consumption of high-quality, sustainably sourced seafood.

Preview Dataset .csv:
![image](https://github.com/roniantoniius/Manettas-RAG-Chatbot-with-Zephyr-7B/assets/121453378/5902314e-ed6a-4857-8577-a067aad4f607)


## RAG: Retrieval-Augmented Generation with Zephyr-7B β
![RAG Framework](https://github.com/roniantoniius/Manettas-RAG-Chatbot-with-Zephyr-7B/assets/121453378/89861d55-58e2-4842-a5df-f40e16db53af)


The proposed solution for the Manettas Online Seafood Market Chatbot utilizes the Retrieval-Augmented Generation (RAG) technique, integrated with the Zephyr-7B β model from Hugging Face. RAG combines both retrieval-based and generation-based approaches to provide informative and contextually relevant responses to user queries/prompt.

![diagram](https://github.com/roniantoniius/Manettas-RAG-Chatbot-with-Zephyr-7B/assets/121453378/31fb08c8-fc92-4176-ad7e-de3815c0490e)


### Retrieval Component
The retrieval component of RAG is implemented using LangChain, specifically leveraging its document retrieval capabilities. In the implementation, the available product information from Manettas, such as product descriptions, is indexed using Pinecone for efficient retrieval. This retrieval component retrieves relevant documents based on the user's query context, ensuring that the chatbot has access to a wide range of information to generate accurate responses.

### Generation Component
The generation component of RAG is powered by the Zephyr-7B β model, a language model fine-tuned for conversational assistance tasks. This model is responsible for generating detailed and comprehensive responses to user queries. By employing techniques such as temperature sampling, top-k sampling, and top-p sampling, the Zephyr model produces diverse and contextually appropriate responses that enhance the conversational experience.

### LangChain Integration
LangChain serves as the orchestrator that integrates the retrieval and generation components seamlessly. It facilitates the flow of information between the retrieval and generation stages, ensuring that the retrieved documents are utilized effectively to enrich the generation process. Through LangChain, the retrieved documents serve as valuable context inputs for the Zephyr model, enabling it to generate more informative and relevant responses.

By combining the retrieval capabilities of LangChain with the generative power of the Zephyr-7B β model, the Manettas Chatbot delivers personalized and insightful responses to user queries, enhancing the overall user experience and promoting engagement with the online seafood market platform.
To start this application:

create virtual environment
```
python -m venv venv
```

activate env
```
.\venv\Scripts\activate
```

dont forget to install several library
```
pip install -r requirements.txt
```

if u want it on docker
```
docker build -t chatbot_manettas .
```

Run
```
streamlit run steamlit.py
```

## Documentation
![image](https://github.com/roniantoniius/Manettas-RAG-Chatbot-with-Zephyr-7B/assets/121453378/64d03cc5-525c-404f-86ac-796020ad6f36)

![image](https://github.com/roniantoniius/Manettas-RAG-Chatbot-with-Zephyr-7B/assets/121453378/9531d4df-f2db-4d0c-b0ad-41f1e4055888)

![image](https://github.com/roniantoniius/Manettas-RAG-Chatbot-with-Zephyr-7B/assets/121453378/33dcc5e8-6c6d-4b41-a394-020d0562731e)


## Deployment
I already deploy the chatbot on streamlit cloud. So if u guys want to see it, lemme know on dm.


### Further Improvement:
- implement semantic search
- use different model
