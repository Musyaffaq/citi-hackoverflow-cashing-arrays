import os
import re
import json
from dotenv import load_dotenv
from langchain import OpenAI, PromptTemplate, LLMChain
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.mapreduce import MapReduceChain
from langchain.prompts import PromptTemplate
from langchain.docstore.document import Document
from langchain.chains.summarize import load_summarize_chain
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("API_KEY")

data = ["""Elon Musk's father told The U.S. Sun he feared his billionaire son could be assassinated.

The 77-year-old Errol Musk criticized a recent article in The New Yorker that explored the world's richest person's influence on government decisions about the war in Ukraine.

Pentagon officials told The New Yorker that Elon Musk was treated like an "unelected official" and raised concerns about his attitude toward Vladimir Putin. The report also highlighted how crucial SpaceX's Starlink satellites had been in the war in Ukraine.

"It's a hit job, a shadow government-sponsored opening salvo on Elon," the elder Musk told The U.S. Sun.

And when The U.S. Sun reporter asked whether he feared the "shadow government" could assassinate his son, he replied, "Yes."

The SpaceX CEO appears to have a strained relationship with his father and has previously called him a "terrible human being."

Errol Musk also described the New Yorker article to The U.S. Sun as "the artillery-like softening up of the enemy before the actual attack."

In May of last year, the billionaire appeared to joke that he could "die under mysterious circumstances" following an argument with Russia's space chief over SpaceX giving Starlink terminals to Ukrainian soldiers.

An X engineer previously told the BBC that two bodyguards had followed Elon Musk around the company headquarters, including to the bathroom. A lawsuit filed in May said he'd also requested a bathroom to be built next to his X office so he wouldn't have to wake up his security in the middle of the night.

But Elon Musk's own security concerns were most apparent during the controversy over his private jet being tracked last December. Journalists who shared links to the @ElonJet account on X, formerly known as Twitter, were temporarily barred, and Musk accused them of wanting to harm him.

That was after Elon Musk said a car carrying his son had been followed by a "crazy stalker (thinking it was me)."

Musk did not immediately reply to a request for comment from Insider, sent outside US working hours."""]

class insight_Generator():

    def __init__(self):
        self.llm = OpenAI()
        self.text_splitter = CharacterTextSplitter(separator="\n", chunk_size=500, chunk_overlap=50)
        self.prompt_template_insight = """Generate investment related insights from the article below. 
        THEN, generate a python list with the top 20 tags that could affect the stock price.
        

        {text}


        --EXAMPLE--
        INSIGHTS: "Insight here"
        LIST OF CATEGORIES: ['tag 1', 'tag 2', 'tag 3', 'tag 4', 'tag 5', 'tag 6', 'tag 7', 'tag 8', 'tag 9', 'tag 10', 'tag 11', 'tag 12', 'tag 13', 'tag 14', 'tag 15', 'tag 16', 'tag 17', 'tag 18', 'tag 19', 'tag 20']
        """

    def data_splitter(self, data):
        texts = self.text_splitter.split_text(data)
        docs = [Document(page_content=t) for t in texts[:3]]
        return docs



    def run_chain(self, data):
        insight_list = []
        tags_list = []

        for article in data:
            docs = self.data_splitter(article)
            PROMPT = PromptTemplate(template=self.prompt_template_insight, input_variables=["text"])
            chain = load_summarize_chain(self.llm, chain_type="stuff", prompt=PROMPT)
            chain({"input_documents": docs}, return_only_outputs=False)


            result = chain.run(input_documents=docs)

            pattern_tags = r'\[.*?\]'
            start = result.find("INSIGHT:") + len("INSIGHT:")
            end = result.find("LIST OF CATEGORIES:")
 
            insight = result[start:end].strip()
            tags_raw = re.search(r'\[([^\]]+)\]', result).group()
            tags = ", ".join(tags_raw)

            insight_list.append(insight)
            tags_list.append(tags)

        return insight_list, tags_list


print(insight_Generator().run_chain(data))
