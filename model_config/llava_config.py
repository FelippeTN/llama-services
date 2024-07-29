from llama_cpp import Llama
from llama_cpp.llama_chat_format import Llava15ChatHandler

def llava_llm():
    chat_handler = Llava15ChatHandler(clip_model_path="llms/llava-phi3-mini-mmproj-f16.gguf")

    llm = Llama(
    model_path="llms/llava-phi3-mini-Q4_K_M.gguf",
    chat_handler=chat_handler,
    n_ctx=2048, # n_ctx should be increased to accomodate the image embedding
    )