# from llama_cpp import Llama
import logging

import pandas as pd

### Open-source LLMs
from transformers import AutoModel, pipeline

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)
logger.addHandler(logging.StreamHandler())


# llm = Llama(model_path="./models/7B/llama-model.gguf")
model_name = "TheBloke/Llama-2-70B-Chat-GPTQ"
generator = pipeline("text-generation", model=model_name, device_map="auto")

prompt = "The Generative AI World Summit is a"
response = generator(prompt, do_sample=False, max_new_tokens=25)
# logger.info(response)
