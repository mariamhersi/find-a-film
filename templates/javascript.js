var quotes = [
  'The Dark Knight',
  'Inception',
  'The Departed',
  'Heat',
  'Leon: The Professional',
  'Black Swan',
  'Kill Bill: Vol 1',
  'The Dark Knight Rises',
  'The Silence of the Lambs',
  'Shutter Island',
  'The Godfather',
  'The Lord of the Rings: The Return of the King',
  'Pulp fiction',
  'Schindlers List',
  'Fight Club',
  'Code First Girls',
  'Avengers End Game'

]

function newMovie() {
  var randomNumber = Math.floor(Math.random() * (quotes.length));
  document.getElementById('MovieDisplay').innerHTML = quotes[randomNumber];
}
