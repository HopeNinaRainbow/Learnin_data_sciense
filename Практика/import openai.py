import openai
# указываем ключ из личного кабинета openai
openai.api_key = "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"
messages = []
while True:
    message = input("User: ")   # вводим сообщение
    if message == "quit": break
     
    messages.append({"role": "user", "content": message})
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages = messages)
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role":"assistant", "content": reply})