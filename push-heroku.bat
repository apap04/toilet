rem this pushes all code to origin and heroku
git add .
git commit -s -m "automated push to heroku and origin"
git push heroku -f
git push origin -f