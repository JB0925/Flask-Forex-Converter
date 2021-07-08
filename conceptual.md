### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
A). Python is a server side language, while JavaScript is predominantly a client side language. Python will throw an error if a function is called with missing parameters, while JS will not. Python has a more full standard library, while JS libraries are imported. Python has more mutable data types than JS.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  A). You can do it with the ".get()" method, or with a try / except block, also known as error handling.

- What is a unit test?
A). A unit test tests a single thing, i.e. "does this function return the correct number?"

- What is an integration test?
A). An integration test combines multiple functions and logic to ensure that the end result from combining them is what is expected.

- What is the role of web application framework, like Flask?
A). A web framework puts into place standards and rules for how to build a web application. They make it easier to build a web app than if you were starting from scratch.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  If you are including data that you know your server will have, then including it as a route parameter might be a good idea. If it is a search, you might include it in the query string.

- How do you collect data from a URL placeholder parameter using Flask?
A). You can use it as a parameter in the route function, and then access it inside of that function.

- How do you collect data from the query string using Flask?
A). You collect data from a query string by using request.args, or request.args.get().

- How do you collect data from the body of the request using Flask?
A). You can use request.get_data() to get data from the body of the request.

- What is a cookie and what kinds of things are they commonly used for?
A). A cookie is a string and is a key value pair. They are used to "remember" things on the pages you've viewed.

- What is the session object in Flask?
A). The session object is like cookies, but not exactly the same. It is a way to store data about the application and keep state, in a sense. The amount of time a session lasts for can be changed.
- What does Flask's `jsonify()` do?
A). Flask's jsonify() is a really handy way to turn data into valid JSON, for it to be returned to a client.
