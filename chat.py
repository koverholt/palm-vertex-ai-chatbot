from vertexai.preview.language_models import ChatModel, InputOutputTextPair


def science_tutoring(temperature=.2):
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

    response = chat.send_message("How many planets are there in the solar system?", **parameters)
    print(f"Response from Model: {response.text}")

science_tutoring()
