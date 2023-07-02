import numpy as np
import pandas as pd
import openai
import tiktoken
import pickle
from nomic import atlas
from tenacity import retry, wait_random_exponential, stop_after_attempt
from dotenv import dotenv_values
config = dotenv_values('../.env')
# Configure Open AI Key:
openai.api_key = config['API_KEY']
data_path = 'movies_plots.csv'
estimator = tiktoken.encoding_for_model('text-embedding-ada-002')


def read_data(path):
    """Create Pandas dataset from file"""
    return pd.read_csv(path)


def keep_n_movies_by_year(df, n):
    """Subset only n american movies"""
    _filter = df['Origin/Ethnicity'] == 'American'
    return df[_filter].sort_values('Release Year', ascending=False).head(n)


@retry(wait=wait_random_exponential(min=1, max=20), stop=stop_after_attempt(6))
def get_embedding(txt, model='text-embedding-ada-002'):
    """Create numerical vector representation for a text"""
    txt = txt.replace('\n', ' ')
    embedding = openai.Embedding.create(
        input=txt,
        model=model
    )
    return embedding['data'][0]['embedding']


def estimate_costs(values, encoder):
    "If needed, Estimate costs for API calls for a given encoder"
    cost = .0001/1000
    tokens = sum([len(encoder.encode(value)) for value in values])
    return f'Estimated Cost: {round(cost * tokens,5)}$'


# Create and prepare Pickle file for the embeddings
pckl_path = 'movies_plots_emb.pkl'

try:
    cache = pd.read_pickle(pckl_path)
except FileNotFoundError:
    cache = {}
with open(pckl_path, 'wb') as file:
    pickle.dump(cache, file)


def embed_plot(plot, emb_cache=cache, model='text-embedding-ada-002'):
    "Create numerical representation dor a plot as a text, then write it into Pickle file"
    if (plot, model) not in emb_cache.keys():
        emb_cache[(plot, model)] = get_embedding(plot, model)
        print(f'{plot[:20]} has embedded')
        with open(pckl_path, 'wb') as embedding_file:
            pickle.dump(emb_cache, embedding_file)
    return emb_cache[(plot, model)]


def get_movies_data(dataset, columns, len=None):
    "Return specific movies information as a dictionary, Useful for Atlas legend"
    return dataset[columns].iloc[:len].to_dict('records')


def plot_with_atlas(embeddings, data=None):
    "Create clustering with Nomic Atlas tool"
    project = atlas.map_embeddings(
        embeddings=np.array(embeddings),
        data=data
    )



if __name__ == '__main__':
    df = read_data(data_path)
    df = keep_n_movies_by_year(df, 2500)
    plots = df.Plot.values
    # Should take some time
    emb_plots = [embed_plot(plot) for plot in plots]

    with open(pckl_path, 'rb') as file:
        my_movies_embeddings = list(pickle.load(file).values())

    print('Total movies from embeddings: ', len(my_movies_embeddings))

    movies_data = get_movies_data(df, ['Title', 'Genre'], len(my_movies_embeddings))
    # print(my_movies_embeddings[3])
    plot_with_atlas(
        my_movies_embeddings,
        movies_data
    )

