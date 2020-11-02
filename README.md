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
