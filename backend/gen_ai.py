import os
from dotenv import load_dotenv
from langchain import OpenAI, PromptTemplate, LLMChain
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.mapreduce import MapReduceChain
from langchain.prompts import PromptTemplate
from langchain.docstore.document import Document
from langchain.document_loaders import JSONLoader
from langchain.chains.summarize import load_summarize_chain
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("API_KEY")

class insight_Generator():

    def __init__(self):
        self.llm = OpenAI()
        self.text_splitter = CharacterTextSplitter(separator="\n", chunk_size=500, chunk_overlap=50)
        self.loader = JSONLoader(file_path='newsapioutput.json', jq_schema='.messages[].content')
        self.prompt_template = """Generate insights from the article below with relation to investment, 
        THEN, generate a list of the top 5 categories that best describes the article.
        

        {article}


        --EXAMPLE--
        INSIGHTS: "Insight here"
        LIST OF CATEGORIES: [list of categories here]
        """

    def data_splitter(self):
        data = self.loader.load()
        articles = data['articles']
        for article in articles:
            texts = self.text_splitter.split_text(article)
            self.docs = [Document(page_content=t) for t in texts[:3]]



    def run_chain(self, data):
        articles = self.data_splitter()
        PROMPT = PromptTemplate(template=prompt_template, input_variables=["article"])
        chain = load_summarize_chain(llm, chain_type="stuff", prompt=PROMPT)
        chain({"input_documents": articles}, return_only_outputs=False)


        result = chain.run(input_documents=docs)

        return result