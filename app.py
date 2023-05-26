import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from vertexai.preview.language_models import ChatModel, InputOutputTextPair

def science_tutoring(message, temperature=.2):
    chat_model = ChatModel.from_pretrained("chat-bison@001")
    parameters = {
    "temperature": temperature,
    "max_output_tokens": 256,
    "top_p": 0.95,
    "top_k": 40,
    }

    chat = chat_model.start_chat(
        context="My name is Miles. You are an astronomer, knowledgeable about the solar system.",
        examples=[
            InputOutputTextPair(
                input_text='How many moons does Mars have?',
                output_text='The planet Mars has two moons, Phobos and Deimos.',
            ),
        ]
    )

    response = chat.send_message(message, **parameters)
    print(f"Response from Model: {response.text}")
    return response.text

st.set_page_config(page_title="A Streamlit chatbot app powered by the PaLM API in Google Cloud")

# Sidebar contents
with st.sidebar:
    st.title('PaLM Chat')
    st.markdown('''
    ## About
    This app is an LLM-powered chatbot built using:
    - [Streamlit](https://streamlit.io/)
    - PaLM API in Vertex AI in Google Cloud

    💡 Note: No API key required!
    ''')
    add_vertical_space(5)

# Generate empty lists for generated and past.
## generated stores AI generated responses
if 'generated' not in st.session_state:
    st.session_state['generated'] = ["I'm a chatbot powered by Google Cloud, How may I help you?"]
## past stores User's questions
if 'past' not in st.session_state:
    st.session_state['past'] = ['Hi!']

# Layout of input/response containers
input_container = st.container()
colored_header(label='', description='', color_name='blue-30')
response_container = st.container()

# User input
## Function for taking user provided prompt as input
def get_text():
    input_text = st.text_input("You: ", "", key="input")
    return input_text
## Applying the user input box
with input_container:
    user_input = get_text()

# Response output
## Function for taking user prompt as input followed by producing AI generated responses
def generate_response(prompt):
    chatbot = science_tutoring(prompt)
    response = science_tutoring(prompt)
    return response

## Conditional display of AI generated responses as a function of user provided prompts
with response_container:
    if user_input:
        response = generate_response(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)

    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))
