import textwrap
from dotenv import dotenv_values
import openai
import pandas as pd
import pickle
import random
import argparse
from openai.embeddings_utils import distances_from_embeddings, indices_of_nearest_neighbors_from_distances

config = dotenv_values('../.env')
# Configure Open AI Key:
openai.api_key = config['API_KEY']
parser = argparse.ArgumentParser()

parser.add_argument('-mn', type=str, help="Movie name")
parser.add_argument('-mi', type=int, help='Movie Index')
parser.add_argument('-n', type=int, help='How many recommendations do you want')

args = parser.parse_args()

with open('movies_plots_emb.pkl', 'rb') as file:
    embeddings = list(pickle.load(file).values())
    file.close()


def get_movie(idx: int = None, movie: str = None):
    """Get movie data from dataset, by support index or name"""
    data = pd.read_csv('movies_plots.csv')
    data_ = data[['Title', 'Genre', 'Plot']]

    if idx and movie is None:
        return idx, data_.iloc[idx]

    elif idx is None and movie:
        idx = data_[data_['Title'] == movie].index[0]
        return idx, data_.iloc[idx]
    else:
        idx = random.randint(0, 1500)
        return idx, data_.iloc[idx]


def read_embeddings(idx):
    """Return vector for given movie index"""
    return embeddings[idx]


def get_distances(idx):
    """Calculate distances for a given vector"""
    return distances_from_embeddings(read_embeddings(idx), embeddings)


def get_indices(distances):
    """Order the distance indices in ascending order"""
    return indices_of_nearest_neighbors_from_distances(distances)


def colortext(text, color='red'):
    """Print with color"""
    if color == 'red':
        return f"\033[91m {text}\033[00m"
    elif color == 'purple':
        return f"\033[95m {text}\033[00m"
    else:
        return text


def recommendation(indices, distances, n):
    """For a given movie, give recommendation for n other movies, return their plot."""
    rec = 1
    for idx in indices[1:n]:
        info = get_movie(idx)[1]
        print(colortext(f'Rec #{rec}', 'red'), colortext(f'{info.Title}', 'purple'))
        print(f'Genre: {info.Genre}')
        print(f'Distance: {round(distances[idx], 3)}')
        print(textwrap.fill(f'Plot: {info.Plot}', break_long_words=False, width=70))
        rec += 1


def main(idx=None, movie_name=None, n=3):
    if idx:
        i, a = get_movie(idx=idx)
    elif movie_name:
        i, a = get_movie(movie=movie_name)
    else:
        i, a = get_movie(random.randint(0, 1299))

    print(colortext('Chosen Movie', 'red'), colortext(a['Title'], 'purple'))
    print(f'Genre: {a["Genre"]}')
    print(textwrap.fill(a['Plot'], break_long_words=False, width=90))
    print('--------------------------------------')
    # a_em = read_embeddings(idx)
    distances = get_distances(i)
    indices = get_indices(distances)
    recommendation(indices, distances, n)


if __name__ == '__main__':
    if args.mn:
        main(movie_name=args.mn, n=args.n)

    elif args.mi:
        main(idx=args.mi, n=args.n)
