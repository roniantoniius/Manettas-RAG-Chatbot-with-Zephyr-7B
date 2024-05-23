import streamlit as st
from main import ChatBot_Manettas

bot = ChatBot_Manettas()
    
st.set_page_config(page_title="Manettas RAG Chatbot with Zephyr-7B-β",
                   page_icon="🐟",
                   layout="wide")

with st.sidebar:
    st.image('logo_noline.png')
    st.title('Market Fresh Seafood')
    st.subheader('Delivered to your Door')

    st.markdown('<a href="https://www.manettas.com.au/" style="text-decoration:none;"><h3>Home</h3></a>', unsafe_allow_html=True)
    
    kategori_list = ['Cured, Smoke & Caviar',
                'Sashimi & Sushi',
                'Ready to Cook',
                'Fruit & Vegetables',
                'Fish - Fillets, Cutlets & Tails',
                'Whole Fish',
                'Prawn',
                'Oysters',
                'Crab & Lobsters',
                'Mussels, Bugs & Shellfish',
                'Calamari & Octopus',
                'Mixed Seafood Packs']
    
    st.markdown("### Product Category")
    kategori = st.selectbox("Choose a category", kategori_list)


    st.title('Zephyr-7B-β')
    st.image('zephyr_beta.png')
    st.write("""
            Zephyr is a series of language models that are trained to act as helpful assistants. Zephyr-7B-β is the second model in the series, and is a fine-tuned version of mistralai/Mistral-7B-v0.1 that was trained on a mix of publicly available data.
             """)

# Function for generating LLM response
def generate_response(input):
    result = bot.rag_chain.invoke(input)
    return result

st.title("Manettas Online Seafood Market Chatbot")
st.image('judul.png')

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "Welcome, let's talk about our seafood products"}]

# Display chat messages
for message in st.session_state.messages:
    if message["role"] == "assistant":
        with st.chat_message("assistant", avatar="logo.jpeg"):
            st.write(message["content"])
    else:
        with st.chat_message(message["role"]):
            st.write(message["content"])

# User-provided prompt
if input := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": input})
    with st.chat_message("user"):
        st.write(input)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant", avatar="logo.jpeg"):
        with st.spinner("Getting information about our seafood product.."):
            response = generate_response(input)
            st.write(response) 
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)
