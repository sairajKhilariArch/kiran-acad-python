



# * To select from a different column and same or different fields value ::

# ^ sqlite> select * from flights where origin is 'pune' or destination = 'pune';



# * To select from a column with multiple fields value match...

# ^ sqlite> select * from flights where origin in ('pune','delhi');




# * To select from a column with a set of match character is present in a field of that column...

# ^ sqlite> select * from flights where origin like '%i%';


