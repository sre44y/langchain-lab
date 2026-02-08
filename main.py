from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

def run():
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    resp = llm.invoke("Say hello in 1 sentence and ask me what project I'm building.")
    print(resp.content)
    
    resp = llm.invoke(" Say a joke to lighten my mood.")
    print(resp.content)
if __name__ == "__main__":
    run()

## Git test

## test-branch

## github checkin -1 

## github checkin -2