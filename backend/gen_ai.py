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

news_articles = [
    {
        'content': 'Nvidia, Tesla, Apple Stocks All Had a Great Week. Bring On SeptemberIt was a good week for the stock market heading into Labor Day as August ended in strong fashion and Friday’s jobs report ensured a solid star... #laborday',
        'url': 'https://biztoc.com/x/e3f6805654e0cdcc',
        'date': '2023-09-04T14:12:07Z'
        },
    {
        'content': "'Low Polygon Joke:' Designer Blasts Tesla’s Cybertruck, Claims It Will Require Complete RedesignA car designer claims Tesla's Cybertruck has a serious problem that can only be fixed with a complete revamp of the vehicle, as its issues are deeply rooted in its design.",
        'url': 'https://www.breitbart.com/tech/2023/09/04/low-polygon-joke-designer-blasts-teslas-cybertruck-claims-it-will-require-complete-redesign/',
        'date': '2023-09-04T14:10:59Z'
        }, 
    {
        'content': 'Neoliberalism on Trial: Artificial Intelligence and Existential Risk<ul>\n<li>Rather than breaking capitalism… A.G.I… is more likely to create a powerful… ally for capitalism’s most destructive creed: neoliberalism.</li>\n</ul>\n<ul>\n<li>—Evgeny Morozov. The New York Times1</li>\n</ul>\nThe New York Times for decades has been Amer…',
        'url': 'https://www.econlib.org/library/columns/y2023/donwayai.htm',
        'date': '2023-09-04T14:00:34Z'
        }, 
    {
        'content': "UAW's clash with Big 3 automakers shows off a more confrontational union as strike deadline loomsA 46% pay raise. A 32-hour week with 40 hours of pay. A restoration of traditional pensions.",
        'url': 'https://www.startribune.com/uaws-clash-with-big-3-automakers-shows-off-a-more-confrontational-union-as-strike-deadline-looms/600301900/',
        'date': '2023-09-04T14:00:08Z'
        }, 
    {
        'content': 'UAW clash with automakers shows more confrontational union as strike looms...A 46% pay raise. A 32-hour week with 40 hours of pay. A restoration of traditional pensions. The demands that a more combative United Auto Workers union has pressed on General Motors, Stellantis and Ford are edging it closer to a strike when its contract ends…',
        'url': 'https://apnews.com/article/automakers-cars-strike-pay-uaw-union-detroit-349a6e7281f1b07710cfcad511dcaa05',
        'date': '2023-09-04T14:00:05Z'
        }, 
    {
        'content': 'Mercedes CLA Concept Takes Efficiency To A New LevelMercedes brought its CLA Concept to the IAA show this week. It borrows many of the technical features of the EQXX experimental car.',
        'url': 'https://cleantechnica.com/2023/09/04/mercedes-cla-concept-takes-efficiency-to-a-new-level/',
        'date': '2023-09-04T13:59:48Z'
        }, 
    {
        'content': 'UAW’s clash with Big 3 automakers shows off a more confrontational union as strike deadline loomsA 46% pay raise. A 32-hour week with 40 hours of pay. A restoration of traditional pensions. The demands that a more combative United Auto Workers union has pressed on General Motors, Stellantis and Ford are edging it closer to a strike when its contract ends…',
        'url': 'https://www.denverpost.com/2023/09/04/uaws-clash-with-big-3-automakers-shows-off-a-more-confrontational-union-as-strike-deadline-looms/',
        'date': '2023-09-04T13:57:03Z'
        }, 
    {
        'content': 'Nvidia, Tesla, Apple Stocks All Had a Great Week. Bring On SeptemberIt was a good week for the stock market heading into Labor Day as August ended in strong fashion and Friday’s jobs report ensured a solid star... #laborday',
        'url': 'https://biztoc.com/x/6b009398fb18a931',
        'date': '2023-09-04T13:44:27Z'
        }, 
    {
        'content': "'Magnificent 7' Give Markets Hope for SeptemberThis month is historically difficult for stocks. Investors will be hoping the momentum of several big companies can continue.",
        'url': 'https://www.barrons.com/articles/nvidia-tesla-apple-stock-market-movers-september-80edcfaf',
        'date': '2023-09-04T13:37:41Z'
        }, 
    {
        'content': "Elon Musk Is Not Satoshi Nakamoto Because 'Bitcoin Whitepaper Has No Memes,' Says DogeDesignerDogeDesigner, as the name suggests, graphic designer at Dogecoin DOGE/USD on Sunday firmly denied the speculation that Elon Musk, the CEO of Tesla and SpaceX, is the elusive creator of Bitcoin BTC/USD known as Satoshi Nakamoto. What Happened: DogeDesigner arg…",
        'url': 'https://biztoc.com/x/062e06b2ae30a00e',
        'date': '2023-09-04T13:36:11Z'
        }
]


class insight_Generator():

    def __init__(self):
        self.llm = OpenAI()
        self.text_splitter = CharacterTextSplitter(separator="\n", chunk_size=500, chunk_overlap=50)
        self.prompt_template_insight = """Generate investment related insights from the article below. 
        THEN, generate a list of the top 20 tags that could affect the stock price.
        

        {text}


        --EXAMPLE--
        INSIGHTS: "Insight here"
        LIST OF CATEGORIES: "tag 1, tag 2, tag 3, tag 4, tag 5, tag 6, tag 7, tag 8, tag 9, tag 10, tag 11, tag 12, tag 13, tag 14, tag 15, tag 16, tag 17, tag 18, tag 19, tag 20"
        """
        self.prompt_template_sum = """Generate a detailed summary of all the insights below:
        

        {text}


        --EXAMPLE--
        INSIGHT SUMMARY: "Insight summary here"
        """


    def data_splitter(self, data):
        texts = self.text_splitter.split_text(data)
        docs = [Document(page_content=t) for t in texts[:3]]
        return docs



    def run_chain(self, news_articles):
        insight_list = []
        tags_list = []

        for i, article in enumerate(news_articles):

            docs = self.data_splitter(article['content'])
            PROMPT = PromptTemplate(template=self.prompt_template_insight, input_variables=["text"])
            chain = load_summarize_chain(self.llm, chain_type="stuff", prompt=PROMPT)
            chain({"input_documents": docs}, return_only_outputs=False)


            result = chain.run(input_documents=docs)

            start = result.find("INSIGHT:") + len("INSIGHT:")
            end = result.find("LIST OF CATEGORIES:")
            start2 = end + len("LIST OF CATEGORIES:")
 
            insight = result[start:end].strip()
            tags_raw = result[start2:].strip()
            news_articles[i]['tags'] = tags_raw

            insight_list.append(insight)

        sum_insights_raw = "\n\n".join(insight_list)
        docs = self.data_splitter(sum_insights_raw)
        PROMPT_SUM = PromptTemplate(template=self.prompt_template_sum, input_variables=["text"])
        chain = load_summarize_chain(self.llm, chain_type="stuff", prompt=PROMPT_SUM)
        sum_insights = chain.run(input_documents=docs)
        return sum_insights, news_articles



print(insight_Generator().run_chain(news_articles))
