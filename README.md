# Ecommerce-product-recommendation-system

Product Recommendation System is a machine learning-based project that provides personalized product recommendations to users based on their browsing and purchase history. The system utilizes collaborative filtering and content-based filtering algorithms to analyze user behavior and generate relevant recommendations. This project aims to improve the overall shopping experience for users, increase sales for e-commerce businesses

## Dataset

I have used an amazon dataset on user ratings for electronic products, this dataset doesn't have any headers. To avoid biases,  each product and user is assigned a unique identifier instead of using their name or any other potentially biased information.

* You can find the [dataset](https://www.kaggle.com/datasets/vibivij/amazon-electronics-rating-datasetrecommendation/download?datasetVersionNumber=1) here - https://www.kaggle.com/datasets/vibivij/amazon-electronics-rating-datasetrecommendation/download?datasetVersionNumber=1 

* You can find many other similar datasets here - https://jmcauley.ucsd.edu/data/amazon/
* Here the data set should be saved in the main branch


## Approach

### **1) Similarity based Collaborative filtering**
Objective -
* Provide personalized and relevant recommendations to users.

Outputs -
* Recommend top 5 products based on interactions of similar users.

Approach -
* Here, user_id is of object, for our convenience we convert it to value of 0 to 1539(integer type).
* We write a function to find similar users - 
  1. Find the similarity score of the desired user with each user in the interaction matrix using cosine_similarity and append to an empty list and sort it.
  2. extract the similar user and similarity scores from the sorted list 
  3. remove original user and its similarity score and return the rest.
* We write a function to recommend users - 
  1. Call the previous similar users function to get the similar users for the desired user_id.
  2. Find prod_ids with which the original user has interacted -> observed_interactions
  3. For each similar user Find 'n' products with which the similar user has interacted with but not the actual user.
  4. return the specified number of products.

## How to deploy in the local system?

*I have used the default flask app to run and deploy in the terminal.  
* Here after running the the main .ipynb file at last save the "final_ratings_matrix.csv" in the main directory.  
* Replace appropriate file paths in the project, in your own system file paths after downloading the files like datasets and "final_ratings_matrix.csv"  
## **Steps to run the flask app:**
  1. run the **run_app.py**.
  2. after succesfull running you will get the message as - 
     ![alt text](https://github.com/sarveshadithya17/E-commerce_product_recommendation_system/blob/3cae428be2f1d89a4d2631fac8046ff82f07746e/succesfull_running.png?raw=true)
  3. Open terminal and enter the following command:  
     **$response = Invoke-RestMethod -Uri http://127.0.0.1:5000/recommend -Method POST -ContentType "application/json" -Body '{"user_id": 3, "num_products": 5}'  
       $response | Out-File -FilePath "recommendations.json"**
  4. Then you will get the required recommendation from the model.

| ⚠️  This project is solely for learning how recommedation systems work. ⚠️ |
|-----------------------------------------------------------------------------|
