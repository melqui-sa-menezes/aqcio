# Python Developer Challenge

### 1. We need you to implement a variation of Javascript’s parseInt() function to handle hexadecimal numbers. Let’s call it parseHexInt(), where:
- parseHexInt(“A”) == 10
- parseHexInt(“1F”) == 31
- parseHexInt(“0”) == 0 

Note: you have to implement the code that converts a string in int. You cannot use parseInt nor int(text, 16). Input will always be valid (e.g. non-empty strings containing chars from 0 to 9 and from A to F) non-negative numbers.

### 2. Given a list of integers, find two numbers whose sum is the largest among all possible sums.
#### Example:
```
[1, 10, 3, 7, 9] => 10 + 9 = 19
[-2, 1, -1, 0] => 1 + 0 => 1
```
Note: input will always have at least two items. Your algorithm can scan the input only once. Hint:
you should not sort it.

### 3. BONUS: Please implement sqrt() using only loops, ifs, addition, subtraction, multiplication and division. 
#### Example:
```
sqrt(9.0) = 3.0
sqrt(2.0) = 1.4142
```
Hint: This can be modeled as a search problem and the solution is between the input number and
1.0.

### 4. Why JSON is better than XML?

The answer to this question is not so simple.
Being often considered "old", XML has characteristics that go beyond the processing and transport of data, being, consequently, more complex. JSON is faster and easier to use. However, while XML is even slower and more complex, it also offers additional features that, to this day, JSON has not yet been developed further.
On the other hand, JSON is a more modern approach to the same purpose as XML, being preferred for delivering data between browsers and servers because of the lighter and faster files it produces.

### 5. Please tell me about the most important/interesting project you worked on. Why was it important? Which programming language you used? Why you believe you were vital for it?
My last job gave me the challenge of working on building a product from scratch. Using the python language, the FastAPI framework and the sqlalchemy ORM, we built API's that served to feed data about products and user permissions in a social e-commerce.
During the period I was able to evolve in the use of clean architecture and clean code standardization.