touch ./build/.nojekyll && git add -f build/ && git commit -m "Deploy to github pages" && git subtree push --prefix build origin gh-pages 
