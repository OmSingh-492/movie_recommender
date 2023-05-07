# movie_recommender
Building a personal movie recommender using Django. [Mainly focused on Back-End Web Development. CSS not used at its fullest. Central usage of CSS is done in generating Bootstrap Cards to display movies on it.]

Choosing an interesting movie to watch on a weekend is always hard. It would be great if there would be a handy movie recommender to help make a good decision. Here, we shall build such a Movie Recommender using Django web framework. The movie recommendation shall be bassed on the movies previously watched by the user. 

The user would need to update the movies which he has already watched from the Django Admin webpage, by setting Watched=True therein on the webpage. Based on the past watch history of the user, we shall be using Jaccard Similarity algorithm to recommend the user movies similar to the ones he has already watched!

Assumption: One would like a new movie if he has watched similar movies before (Content filtering based model).
