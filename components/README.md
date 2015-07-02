
Top level pages such as:
/data/Company
/data/Project

are controlled under the 
services/data/ directory

The html.template conatins a set of 'if' statements that selects html
depending on the arg0 of the path (Company, Project, etc)
Because the templating engine does not have an elif function, we can't
set a default, therefore any new top level elements must be explicitly 
created.


Individual Projects/Companies etc
These are controlled under /types
