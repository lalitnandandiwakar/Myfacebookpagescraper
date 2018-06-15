import bonobo

graph = bonobo.Graph(
    bonobo.CsvReader('Google_facebook_statuses.csv'),
    bonobo.JsonWriter('output.json'),
)

if __name__ == '__main__':
    bonobo.run(graph)