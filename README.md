Source for the [Folded Weekly](https://folded-weekly.netlify.app/) newsletter

## Making a new post
requirements: [hugo](https://gohugo.io/categories/installation/), [pymol](https://github.com/schrodinger/pymol-open-source/), [smartcrop-cli](https://github.com/jwagner/smartcrop-cli)

```shell
hugo new --kind=posts posts/<num>.md
# fill in content in content/posts/<num>.md

./make_post_image.sh <pdb_id> <num> # use lowercase pdb_id

# add <num>_fotw.png to static/img/ and link in post

hugo server # check that everything looks good
hugo --minify # build the site
```
