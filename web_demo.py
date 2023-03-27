from peft import PeftModel
from transformers import LlamaForCausalLM, LlamaTokenizer, GenerationConfig
import streamlit as st
from streamlit_chat import message


st.set_page_config(
    page_title="Chinese-alpaca-lora Demo",
    page_icon=":robot:"
)


@st.cache_resource
def get_model():
    tokenizer = LlamaTokenizer.from_pretrained("decapoda-research/llama-7b-hf")
    model = LlamaForCausalLM.from_pretrained("decapoda-research/llama-7b-hf",load_in_8bit=True,device_map="auto",)
    model = PeftModel.from_pretrained(model, "silk-road/luotuo-lora-7b-0.3")
    model = model.eval()
    return tokenizer, model

tokenizer, model = get_model()

generation_config = GenerationConfig(
    temperature=0.1,
    top_p=0.75,
    num_beams=4,
)

def generate_prompt(instruction, input=None):
    if input:
        return f"""Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
{instruction}

### Input:
{input}

### Response:"""
    else:
        return f"""Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
{instruction}

### Response:"""

def stream_chat(input, history=None):
    if history is None:
        history = []
    
    # join prompt and response in chat history list
    chat_history = ""
    for i, (prompt, response) in enumerate(history):
        chat_history += f"""User: {prompt}\nAI: {response}\n"""
    instruction = generate_prompt(input)
    instruction = chat_history + instruction
    inputs = tokenizer(instruction, return_tensors="pt")
    input_ids = inputs["input_ids"].cuda()
    generation_output = model.generate(
        input_ids=input_ids,
        generation_config=generation_config,
        return_dict_in_generate=True,
        output_scores=True,
        max_new_tokens=256
    )
    for s in generation_output.sequences:
        output = tokenizer.decode(s)
        response_text = output.split("### Response:")[1].strip()

    # Update history
    history.append((input, response_text))
    return response_text, history


MAX_TURNS = 20
MAX_BOXES = MAX_TURNS * 2


def predict(input, history=None):
    if history is None:
        history = []

    with container:
        if len(history) > 0:
            for i, (query, response) in enumerate(history):
                message(query, avatar_style="big-smile",is_user=True, key=str(i) + "_user")
                message(response, avatar_style="bottts", key=str(i))

        message(input, avatar_style="big-smile",is_user=True, key=str(len(history)) + "_user")
        st.write("AI正在回复:")
        with st.empty():
            response, history = stream_chat(input, history)
            query, response = history[-1]
            st.write(response)

    return history


container = st.container()

with st.form(key="instruction_form"):
    # create a prompt text for the text generation
    prompt_text = st.text_area(label="指令",
                height = 100,
                placeholder="请在此输入你的指令.")


    if 'state' not in st.session_state:
        st.session_state['state'] = []

    submit_button = st.form_submit_button("发送")

    if submit_button:
        with st.spinner("正在生成，请稍等........"):
            # text generation
            st.session_state["state"] = predict(prompt_text, st.session_state["state"])

new_chat_button = st.button("新对话")

if new_chat_button:
    st.session_state["state"] = []
    


