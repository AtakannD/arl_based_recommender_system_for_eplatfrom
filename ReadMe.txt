*Association Rule Based Recommender System*


1. Business Problem

Armut, Turkey's largest online service platform, brings together service providers and those who want to receive 
service. It provides easy access to services such as cleaning, modification and transportation with a few touches on your computer or smart phone.
It is desired to create a product recommendation system with Association Rule Learning by using the dataset 
containing the service users and the services and categories these users have received.


2. Story of Dataset

The dataset consists of the services customers receive and the categories of these services. It contains the 
date and time information of each service received.


3. Variables of Dataset

UserId: Customer id
ServiceId: They are anonymized services belonging to each category. (Example: Upholstery washing service under 
Cleaning category) A ServiceId can be found under different categories and refers to different services under 
different categories. (Example: The service with CategoryId 7 and ServiceId 4 is honeycomb cleaning, while the 
service with CategoryId 2 and ServiceId 4 is furniture assembly)
CategoryId: Anonymized categories. (Example: Cleaning, transportation, renovation category)
CreateDate: The date the service was purchased


Task 1: Preparing of Data


	Step 1: Read the csv file

	Step 2: ServiceID represents a different service for each CategoryID. Combine ServiceID and CategoryID 
	to create a new variable to represent these services

	Step 3: The data set consists of the date and time the services are received, there is no basket 
	definition (invoice etc.). In order to apply Association Rule Learning, a basket (invoice, etc.) definition 
	must be created. Here, the definition of basket is the services that each customer receives monthly. 
	For example; A basket of 4_5, 48_5, 6_7, 47_7 services received by the customer with id 25446 in the 
	8th month of 2017; 17_5, 14_7 services received in the 9th month of 2017 represent another basket. 
	Baskets must be identified with a unique ID. To do this, first create a new date variable that 
	contains only the year and month. Combine the UserID and the newly created date variable and assign 
	it to a new variable.


Task 2: Generating Association Rules and Making Suggestions
	

	Step 1: Creating the basket - service pivot table.

	Step 2: Creating association rules.

	Step 3: Making a service recommendation to a user who has received the 2_0 service in the last 1 month.













