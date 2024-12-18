from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

prompt_template=ChatPromptTemplate.from_messages([
    ('system', "{smsg}"),
    ('human',"{hmsg}")
])

chain = prompt_template | llm | StrOutputParser()

result=chain.invoke({'smsg':"You are an excellent teacher who is best at teaching concepts with real world examples" , 'hmsg' : 'what is organic chemistry?'})
print(result)