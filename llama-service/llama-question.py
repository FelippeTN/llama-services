from llama_cpp import Llama
from llama_cpp.llama_chat_format import Llava15ChatHandler

import datetime
import time

from llms_config.llama_config import llama_llm
from llms_config.llava_config import llava_llm

class ChatBot:
    def __init__(self):
        self.llama = llama_llm()
        self.llava = llava_llm()
        pass
        
    def llama_chat(self, message):
        llm = self.llama
        response = llm.create_chat_completion(
            messages = [
            {   "role": "system", "content": ""},
            {
                "role": "user",
                
                "content": f"{message}"
            
                }
            ]
        )
        return print(response)

message = str(input('Mande uma mensagem para o seu bot: '))

chatbot = ChatBot()
chatbot.llama_chat(message)
