from llama_cpp import Llama
import time

model_name = 'meta-llama-3-8b-instruct.Q4_K.gguf'

llm = Llama(
      model_path=f"llms/{model_name}",
      chat_format="llama-3",
      n_gpu_layers=-1, # Uncomment to use GPU acceleration
      seed=42, # Uncomment to set a specific seed
      n_ctx=8090, # Uncomment to increase the context window
      max_new_tokens=8090,
      temperature=0.7,
      n_batch=2048,
      n_threads=8,
      n_threads_batch=8,
)

inicio = time.time()

response = llm.create_chat_completion(
        messages = [
          {   "role": "system", "content": ""},
          {
              "role": "user",
               
               "content": ""
           
          }
      ]
)
fim = time.time()

print("############################")
print(response)

execution_time_seconds = fim - inicio
execution_minutes = int(execution_time_seconds // 60)
execution_seconds = int(execution_time_seconds % 60)
print(f"Tempo de execução: {execution_minutes} minutos e {execution_seconds} segundos")


