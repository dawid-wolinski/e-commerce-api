**Basic information**

eCommerce API is organised around RESTful principles. It resembles online shopping platforms, such as Amazon, eBay or Allegro, where users can sell and buy their products.

The API was created using Flask web framework. All the data is stored in PostgreSQL database, using SQLAlchemy as an ORM system. The API and database are deployed to Heroku, a cloud platform which allows the API to be accessed from anywhere, at anytime. It is hosted at the following domain: https://api-online-shopping.herokuapp.com/


**Documentation**

https://documenter.getpostman.com/view/19248285/UVeGr62D


**Authorization**

eCommerce API uses an OAuth 2.0 authorization standard. In order to send POST PUT or DEL requests (except account creation and log in), the user has to first create an account and log in using valid credentials. After logging in, the user will receive an access token which will have to be provided alongside aforementioned requests.

The token has to be passed in the request header together with a 'Bearer' keyword, i.e. Bearer .


**Querying**

All GET requests, except those which return a specific item, can include query parameters which take form of filters and sorting arguments.

**Filters**

Results can be filtered based on any attribute of a specific item, except its ID. For example when querying products, the following attributes can be used as filters: "name", "price", "seller_id", "category", "new" and "posted_at" (e.g. .../products?name=laptop&category=electronics).

Additionally, the API supports range filters for numeric attributes which work by adding range type to the name of attribute. The are two range types: "from" (equal or greater than) and "to" (equal or smaller than). For example, to find products in the price range from 200 to 500, the request would be: .../products?price-from=200&price-to=500.

**Sorting**

The query results can also be sorted by providing a "sorting" parameter with a value indicating the attribute to sort by and the sorting order. For example, to list products from newest to oldest, the request would be: .../products?sorting=date-desc.