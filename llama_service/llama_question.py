from llama_cpp import Llama
from llama_cpp.llama_chat_format import Llava15ChatHandler

import datetime
import time
import json

from llms_config.llama_config import llama_llm
from llms_config.llava_config import llava_llm


class ChatBot:
    def __init__(self):
        self.llama = llama_llm()
        self.llava = llava_llm()
        self.response_ia = None

        
    def llama_chat(self, message):
        llm = self.llama
        self.response_ia = llm.create_chat_completion(
            messages = [
            {   "role": "system", "content": "Você é um chat bot ajudante"},
            {
                "role": "user",
                
                "content": f"{message}"
            
                }
            ]
        )
        return self.response_ia
    
    
    def menu_chat(self, response_ia):
        try:
            with open('../data/menu.json', 'r') as file:
                menu = json.load(file)
        except Exception as e:
            print(f"Error reading menu: {str(e)}")
         
        user_option = [] 
        user_question = []
        print("Menu:")
        try:
            while user_option != 4:
                for option in menu["menu"]["options"]:
                    print(f"{option['id']}. {option['title']} - {option['description']}")
                
                user_option = int(input('Escolha uma opção: '))
                if user_option == 1:
                    while user_question != ('sair').lower:
                        user_question = str(input('Faça sua pergunta ao LLAMA\nPergunta:'))
                        self.llama_chat(user_question)
                        response_content = self.response_ia['choices'][0]['message']['content']
                        print(f'\n\n\nResposta IA: {response_content}\n\n\n')
                    
                elif user_option == 2:
                    print("EM DESENVOLVIMENTO...")
                    
                elif user_option == 3:
                    print(f'\n\n\nCriador: {menu["menu"]["options"][2].get("acao")}\n\n\n')
                    
                elif user_option == 4:    
                    break
                
                else:
                    print('Digite uma opção válida.')
                        
        except Exception as e:
            print(f"Error: {str(e)}")    
        


chat = ChatBot()
chat.menu_chat('cavalo')

