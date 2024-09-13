# Portfolio Website
This is my portofolio, it will be a website with all the relevant things about my projects.

# Steps to reproduce
First, create locally a conda environment.
```
conda create --name portofolio python=3.11
```
Activate the environment.
```
conda activate portofolio.
```

Install the requirements.
```
pip install requirements.txt
```

Create the static/styles.css, templates/index.html and app.py files.
Try to run the app locally:
```
python app.py
```

Add Dockerfile. Build it.
```
docker build -t my_portfolio_app .
```
and run it locally:
```
docker run -p 8080:8080 my_portfolio_app
```

