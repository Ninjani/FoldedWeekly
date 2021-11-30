---
title: "Issue {{ replace .Name "-" " " | title }}"
date: {{ .Date }}
showToc: true
TocOpen: true
draft: false
hidemeta: false
comments: false
ShowBreadCrumbs: false
ShowReadingTime: true
summary: |
  This is the summary
cover:
    image: "img/{{ replace .Name "-" " " | title }}.png" # image path/url
    alt: "{{ replace .Name "-" " " | title }}" # alt text
    relative: false # when using page bundles set this to true
---
