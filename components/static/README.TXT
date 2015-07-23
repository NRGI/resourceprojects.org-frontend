This folder can be used to store static documents, such as HTML pages, CSS files and JS code. LODSPeaKr doesn't force you to use it, however, it is considered a good practice to have everything under static/ and not disperse everywhere.

A second benefit is that it will allow other people to reuse your static pages if you decide to export the code. LODSPeaKr will only look on static/ models/ and views/ directories.


TEMPLATED FILES (July 2015)

For easier authoring, a number of pages are maintained as markdown, and converted to HTML before deployment.

Right now, conversion takes place manually with pandoc.

For any files which have a .md equivalent, this should be considered the document to edit.

Run:

```
pandoc file.md -o file.html --template=page.template
```

To set page titles, make sure files begin with a line such as

% Page title