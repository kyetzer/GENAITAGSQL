import pandas as pd
import lotus
from lotus.models import LM
from langchain_groq import ChatGroq
import litellm
import os
# configure the LM, and remember to export your API key, please set any one of the key
os.environ['GROQ_API_KEY'] = "YOUR GROQ_API_KEY"
or
os.environ['GOOGLE_API_KEY'] = "YOUR GOOGLE_API_KEY"

lm = LM(model='groq/llama-3.1-70b-versatile')
rm = SentenceTransformersRM(model="intfloat/e5-base-v2")
reranker = CrossEncoderReranker(model="mixedbread-ai/mxbai-rerank-large-v1")
lotus.settings.configure(lm=lm, rm=rm, reranker=reranker)
# create dataframes with course names and skills
courses_data = {
    "Course Name": [
        "History of the Atlantic World",
        "Riemannian Geometry",
        "Operating Systems",
        "Food Science",
        "Compilers",
        "Intro to computer science",
    ]
}
skills_data = {"Skill": ["Math", "Computer Science"]}
courses_df = pd.DataFrame(courses_data)
skills_df = pd.DataFrame(skills_data)
