import chainlit as cl
from openai import AsyncOpenAI

client = AsyncOpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

@cl.on_chat_start
async def start():
    await cl.Message(content="**Ahrensburg.city**").send()

@cl.on_message
async def main(message: cl.Message):
    response = await client.chat.completions.create(
        model="llama3.1",
        messages=[{"role": "user", "content": message.content}],
        stream=True
    )

    msg = cl.Message(content="")
    
    async for part in response:
        if token := part.choices[0].delta.content:
            await msg.stream_token(token)

    await msg.send()