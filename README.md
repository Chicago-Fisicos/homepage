# Streamlit Webpage
This repository contains the code for a webpage created using Streamlit. 
The webpage serves as an interactive platform to present various physics experiments and their analyses.

The webpage is deployed and can be accessed using any of the following links:
- https://chicago-fisicos.xyz
- https://chicago-fisicos.chewer.net
- https://chicago-fisicos.streamlit.app


## Run locally
To run this project locally, follow these steps:

#### Download the repo
```bash
git clone https://github.com/Chicago-Fisicos/homepage.git
cd homepage
```

#### Run directly with Streamlit
```bash
pip install -r requirements.txt
streamlit run Pages/home.py
```
Once the Streamlit server is running, you can interact with the webpage through your web browser at http://localhost:8501.

#### Or you can run it with docker
Make sure you have Docker and Docker Compose installed on your system.

```bash
docker compose up
```
Open your browser at http://localhost:8505.

