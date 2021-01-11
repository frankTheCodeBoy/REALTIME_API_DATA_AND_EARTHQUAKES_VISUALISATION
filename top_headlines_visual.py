import requests

from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store response.
url='https://newsapi.org/v2/top-headlines?country=us&apiKey=7c7b021589be4e6cb8618f035c0fbb6d'
r = requests.get(url)
print(f"Status Code: {r.status_code}")

# Process the results.
query_dict = r.json()
article_dicts = query_dict['articles']
article_links, labels, content_size = [], [], [],
for article_dict in article_dicts:
    article_title = article_dict['title']
    article_url = article_dict['url']
    article_link = f"<a href= '{article_url}'>{article_title[:15]}...</a>"
    article_links.append(article_link)
    # Extract content of articles and get word count
    try:
        words = article_dict['content'].split()
    except AttributeError:
        pass
    else:
        content_size.append(len(words))
    # Create a custom label
    source = article_dict['source']['name']
    author = article_dict['author']
    description = article_dict['description']
    published = article_dict['publishedAt']
    label = f"{source}<br />{author}<br />{description}...<br />{published}"
    labels.append(label)

    
# Make visualisation.
data = [{
    'type':'bar',
    'x': article_links,
    'y': content_size,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'},
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': "<b>Current Top Headlines in America - RealTime</b>",
    'titlefont': {'size': 28, 'color': 'rgb(0, 0, 128)'},
    'xaxis': {
        'title': '<i>News Articles</i>',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': "<i>Total Word Count<br />of Content-summary</i>",
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='top_usa_news.html') 