## URL SHORTNER
Url shortner is a simple lightweight tool designed for the sole purpose of convinience. It takes long messy urls as user inputs, converts them into short url and provides to the user. Users can then enter that short url and get redirected to the original url. It is fast, simple and reliable. This can be used weather to share urls with your friends(like sharing online game urls) or just shortening a amazon links for your future self.

## How does this work?
It takes a long url as user input. The long url is then passed to the backend. The backend checks if the url is already present in the database and if present, sends the pre-generated short form url to the frontend. If not, then the backend generates a unique 7 digit code for the specific url (and check if that code already exists before) and after all that, combines the short code with the root domain and sends a short links to the user. It also saves the short code in the database along with the long url for future use. Users can then enter the short url in the browser which redirects them to the original link.

## Technologies used in this project
This project is made by using Python-Flask in the backend along with sqlalchemy as ORM and basic html and css in the frontend. Supabase is used for database hosting.

## Why I built this project?
This is mainly a hobby project that I built mostly for myself but everyone can use it. I use urlshortners like tinyurl and bitly A LOT so I just thought why not make my own shortner that I will use. 

## Screenshots: