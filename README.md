In this project, I've implemented a linkedin post simulator that generates realistic post data and runs analytics on it. 

## Features
- Simulated linkedin post data
- Multi-threaded crawler implemntation
- Kafka queue system
- SQLite database
- Data analysis in jupyter notebook
- Docker containerizzation
- poetry for dependence mgmt

## Files 
- data_generator.py- Generates realistic linkedin post data and profile URLs with different media types
- kafka_simulator.py- Simulates kafka queue and implements push/poll operations 
- crawler.py- multi-threaded implementation which discovers and processes profile URLs and post data 
- database.py- SQLite database for persistence 
- pyproject.toml- dependence mgmt 
- analysis.ipynb- jupyter nb for analysis
- dockerfile - for dockerization 

## Generated data structure 

```python
{
    'post_id': str,
    'profile_url': str,
    'content': str,
    'timestamp': datetime,
    'likes': int,
    'comments': int,
    'has_image': bool,
    'has_video': bool,
    'media_type': Optional[str]
}
```

## Prerequisites- Python,Docker,Poetry

## Installation 

1. clone the repo

2. Install dependencies using Poetry
```bash
poetry install
```

3. Build the Docker image:
```bash
docker build -t linkedin-simulator .
```
![image](https://github.com/user-attachments/assets/f30e9105-3d4b-4474-bbad-c76db3c7e544)


### Running the Application

1. **Using Poetry:**
```bash
poetry run python -m linkedin_simulator.main
```
![image](https://github.com/user-attachments/assets/531eb741-3f7f-46ef-8f9e-20990e7884d6)

2. **Using Docker:**
```bash
docker run linkedin-simulator
```

### Running the Analysis

1. Use Jupyter Notebook


## Analysis Metrics

1. **Average Monthly Posting Frequency**
2. **Average Weekly Posting Frequency with trends**
   
![output](https://github.com/user-attachments/assets/b9f9da96-5d55-4257-b1f2-ee428d0615d9)

4. **Distribution of Post Length and Mean**
5. **Distribution of Word Counts and Mean**
   
![output](https://github.com/user-attachments/assets/6c75ac42-320e-4008-8e82-2b9de7ee256b)

6. **Distribution of media types** 
7. **Average likes by media type**
   
![output](https://github.com/user-attachments/assets/ce7d126c-d128-4347-bc55-d4acf0a2b35b)



