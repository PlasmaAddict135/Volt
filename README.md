# Volt
A language built with sole focus on readability, functionality and speed of development!

Here's an example of the fibonacci series generation algorithm written in Volt:
```
fn fibonacci( num ) do
  if num <= 1 do
    return num
    
   else do
      return fibonacci( num - 1 ) + fibonacci( num - 2 )
```

Here's an example of a guess game in Volt:
```
incl (
  random as rd
)

compGuess = rd.gen(1, 100)

loop do
  userGuess = in('Your guess : ')
  if userGuess > compGuess => out('Guess Lower!')
  if userGuess < compGuess => out('Higher!')
  if userGuess == compGuess do
    out('You guessed it!')
    break
```

