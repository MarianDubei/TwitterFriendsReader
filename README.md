# TwitterFriendsReader

The project allows user to look thorough information about required Twitter user. 

After launch user has to type in Twitter user's nickname without '@'. After that they are given highest levels of JSON Object, which contains information about all user's friends. Program also creates JSON file with this JSON Object.

```
> 
[+] users
next_cursor : 1526010764370019775
next_cursor_str : 1526010764370019775
previous_cursor : 0
previous_cursor_str : 0
total_count : None

Enter a key to check its structure, 'back' to return one level back or 'exit' to exit: 
```

User can go to deeper levels by typing in a name of level with its own structure, which can be identified by sign ```[+]``` before it.

```
Enter a key to check, 'back' to return one level back or 'exit' to exit: users


> users > 
Object #0
Object #1
Object #2
Object #3
Object #4

Enter object number to check its structure, 'back' to return one level back or 'exit' to exit: 
```

If level contains not an Object, but a list of other Objects, user has to type number of Object to check its content. To go back on the structure user can type in ```back```.

If use wants to exit program, they can type in ```exit```.
