# Citi HackOverflow 2023 - Cashing Arrays - StockAid

## Problem Statement
In the fast-paced realm of financial markets, real-time risk assessment is paramount to safeguarding investments. However, current risk management tools often lack the narrative context required to comprehensively understand emerging risks and provide insights.

Design a PoC that transforms market data into informative narrative risk insights to equip financial professionals with actionable insights, empowering them to proactively manage risks.

## To Set Up This Project
1. Clone this repository to your local machine
2. Run `cd frontend`
3. Run `npm install` or use `npm install --force` if required
4. Run `cd ../backend`
5. Run `pip install -r requirements.txt`

## Adding your own API Token for the 2 services used
1. Inside the `backend` folder, create a .env file and add in these 2 tokens:
    - `NEWS_API_KEY=` from https://newsapi.org/
    - `API_KEY` from https://openai.com/blog/openai-api

## To run frontend
1. From the root directory, run `cd frontend`
2. Run `npm run start` to start the frontend
3. Access the frontend at `http://localhost:3000/`

## To run the backend
1. From the root directory, run `cd backend`
2. Run `python main.py` to start the backend
3. Access the backend at `http://localhost:5000/`

# Credits
- Frontend UI: https://github.com/creativetimofficial/black-dashboard-react
