# Defense_of_the_Ancient

## About the Dashboard
Displays charts for comparison of heroes and matches

### Run in local environment
``` bash
$ pip install -r requirements.txt
$ python app.py
# visit localhost:2810
```

### Run in docker
``` bash
$ docker-compose up --build
#visit localhost:2810

# End sesssion
$ docker-compose down
```


# Built With
- [Dash](https://dash.plotly.com/) - Main server and interactive components
- [Opendota](https://opendota.com/) - Website to get match and heroes informations
- [Plotly python](https://plotly.com/python/) = Used to create interactive plots