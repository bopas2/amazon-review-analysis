# 6242-Amazon-Reviews-Project -- CSE 6242 Final Project

# Description
This project is a data exploration project for Amazon reviews. After calculating positive or negative review sentiments and determining keywords from amazon reviews, the project groups products that have similar reviews. There is a visualization that allows users to enter a search and explore the most relevant cluster of amazon products relating to that search. In summary, this project groups products by the content of their reviews, and allows users to explore new products through an interactive visualization.

# Installation
First, clone our repository or download our project.

There are two separate parts to our project. The first part is calculating sentiment, determining keywords and creating clusters from a dataset of Amazon reviews. This step is done using a jupyter notebook (found in the review_analysis/code folder). This code can be run in Google Colab and requires no additional installation (the code includes installing libraries and downloading the dataset). 

The second part to our project is the visualization aspect. The visualization is done using a python library called streamlit. First install python3.7 from https://www.python.org/downloads/release/python-370/. Next, you must install the appropriate python libraries being used. You can do this using the command "pip install -r requirements.txt". You may use a virtual environment to accomplish this. After running this command, you have set up your environment to run our project! 

# Execution
There are two steps to running our project. The first step, which groups products together, is done in the Jupyter notebook (found in the review_analysis/code folder). To run this notebook, go to Google Colab (https://colab.research.google.com/) and upload the notebook. For best performance, go to the Tools tab -> Change runtime type -> Hardware accelerator and select GPU. Once uploaded, simply run each cell. The cells will handle downloading libraries and datasets for you. If you want to change the amazon reviews dataset being clustered, you can change the dataset url from "amazon_us_reviews/Mobile_Electronics_v1_00" to the appropriate new dataset url. After each cell's code completes running, which takes multiple hours, the code will generate multiple files that need to be downloaded for visualization purposes. 

The generated files that must be downloaded are: cluster.xlsx, k_means_model.pickle and the sentiment folder. These files contain cluster information and trained models which will be used to visualize the project's results. Once these files are downloaded, we must add them to the source code. Put the k_means_model.pickle and the sentiment files in the pages folder. Put the cluster.xlsx file in the root directory. Finally, after following the instructions above, you can start the visualization by running: "streamlit run startup.py" which will open up the visualization in a new tab on your internet browser. 

An example visualization can be viewed, without running the jupyter notebook in the "Example Queries" tab of the visualization. This visualization uses the search query "Lightweight laptop" and uses the "Mobile Electronics" amazon reviews dataset. The "Custom Queries" is the main visualization for entering custom search terms and visualizing custom datasets.
