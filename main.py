from llama_index.llms.gemini import Gemini
from rich.console import Console
from rich.markdown import Markdown
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
console = Console()
llm = Gemini(
    api_key=API_KEY,
    temperature=0.1,
    max_tokens=2048,
)
while True:
    try:
        question = input("\n>")
        if question == "exit":
            print("bye!")
            break

        stream_complete_response = llm.stream_complete(question)
        response = ""
        for r in stream_complete_response:
            response += r.text

        md = Markdown(response)
        console.print(md)

    except KeyboardInterrupt:
        break
