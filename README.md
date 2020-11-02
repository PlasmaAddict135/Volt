# Volt
A language built with sole focus on readability, functionality and speed of development!

Here's an example of the fibonacci series generation algorithm written in Volt:
```
fn fibonacci( num ) {
  if num <= 1 {
    return num
   } else {
    return fibonacci( num - 1 ) + fibonacci( num - 2 )
   }
}
```

Here's an example of a guess game in Volt:
```
incl {
  random as rd
}

compGuess = rd.gen(1, 100)

loop {
  userGuess = in('Your guess : ')
  if userGuess > compGuess => out('Guess Lower!')
  if userGuess < compGuess => out('Higher!')
  if userGuess == compGuess {
    out('You guessed it!')
    break
  }
}

```
