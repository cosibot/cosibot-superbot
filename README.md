# Cosibot - COVID-19 Stay Informed bot

This project strives to create a chatbot as a information service in the current corona crisis.

*T.B.D*


Project Organization
------------

    ├── cosibot            <- Source code for use in this project.
    │   ├── data           <- Data for training
    │   │   └── NLU.md     <- NLU training data
    │   │   └── stories.md <- Your stories
    |   |
    │   ├── models         <- Trained and compiled models
    │   │  
    │   ├── tests          <- Evaluate chatbot behaviour
    │   │  
    │   ├── actions.py     <- Code for your custom actions
    │   │  
    │   ├── config.yml     <- Configuration of your NLU and Core models
    │   │  
    │   ├── credentials.yml<- Details for connecting to other services
    │   │  
    │   ├── domain.yml     <- Details for connecting to channels like fb messenger
    │   │
    │   └── endpoints.yml  <- Scripts to create exploratory and results oriented visualizations
    │
    ├── test               <- Unit tests 
    ├── Makefile           <- Makefile with useful shell commands 
    ├── README.md          <- The top-level README for developers using this project.
    ├── requirements.txt   <- The requirements file 
    ├── .gitignore         <- Files that shouldn't be uploaded to the repository 
    └── setup.py           <- makes project pip installable (pip install -e .) so cosibot can be imported