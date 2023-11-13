import logging

import streamlit as st
from transformers import pipeline

from llm_logger import LOGGER_NAME, has_stream_handler

logger = logging.getLogger(LOGGER_NAME)
logging.basicConfig(level=logging.DEBUG)
if not has_stream_handler(logger):
    logger.addHandler(logging.StreamHandler())


def prompt_llm(prompt: str):
    """Generate text from the given prompt.

    Arguments:
        prompt: The prompt to generate text from.
    """
    response = generator(prompt, do_sample=False, max_new_tokens=50)
    logger.debug(response)
    return response[0]["generated_text"]


model_name = "TheBloke/Llama-2-7B-Chat-GPTQ"
generator = pipeline(
    "text-generation", model=model_name, framework="pt", device_map="auto"
)

prompt = st.text_input(
    label="Prompt", value="Type in a topic you would like Anki cards for!"
)
if st.button("Run", type="primary"):
    with st.spinner("Wait for it..."):
        response = generator(prompt, do_sample=False, max_new_tokens=25)
        st.write(response[0]["generated_text"])
        st.balloons()
