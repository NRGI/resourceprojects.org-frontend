% Contribute

We’re developing approaches to make it easy for you to contribute data to Resource Projects, either by:

* Submitting new project level reporting data

* Submitting corrections and enhancements to the existing data 

We’ve prepared a simple Google Spreadsheet template that steps you through providing key data on:

* Companies and corporate groupings

* Projects and sites

* Company payments to government, and government receipts

You can [access a copy of the spreadsheet here](https://docs.google.com/spreadsheets/d/19pLirq9l-4W0DudIxb_P5KEMx6HP2smxDksUBVoyQ3I/edit?usp=sharing).

## Using the template

There are four stages to getting data onto the Resource Projects platform. Most of the time you just need to work on stage (1) and (2), and then get in touch and we’ll be able to take it from there. 

### (1) Get your copy

Making sure you are have a [Google Account](http://google.com/accounts/) and are logged in, [follow this link to view the spreadsheet template](https://docs.google.com/spreadsheets/d/19pLirq9l-4W0DudIxb_P5KEMx6HP2smxDksUBVoyQ3I/edit?usp=sharing).

From the file menu, choose ‘Make a copy...’

### (2) Enter data

Work through the instructions in the spreadsheet to enter your data. 

You may wish to copy your source data into a new tab of the sheet.

Once you’ve filled in all your data:

1. Set the sharing settings of your spreadsheet so that anyone can view it;

2. Choose ‘Publish to the web’ from the file menu, and choose ‘Publish’;

If you’re not comfortable with advanced formula and python, then now is the time to get in touch with the Resource Projects team to let us know your data is ready to convert and load onto the platform. 

### (3) Reconcile identifiers

Before the data is loaded, we need to make sure we match key entities to existing data on the platform. 

Essentially, what needs to happen is that all the project, company, group and site records in your data need to be checked against any existing records in ResourceProjects.org and if they are already mentioned there, the ResourceProjects.org identifier needs to be added to your spreadsheet. 

This can be done using the [RDF Open Refine extension](http://refine.deri.ie/) against our SPARQL endpoint (searching on skos:prefLabel), or by exporting a full list of companies, projects, and groups into your spreadsheet, and using query or vlookup formula to reconcile IDs. 

### (4) Convert the data to RDF

This last stage is all a bit rough-and-ready right now, but if you are comfortable with python you will find the tools you need [in this repository](https://github.com/NRGI/resource-projects-etl/) to get from the template to RDF data for loading into the platform. 

Set up the virtual environment, and load all the required tools, and then you will need the script in process/google-docs-reader/

In that folder, run the command:

```
python transform-from-gdocs.py <spreadsheetURI> <identifier>
```

with the web address of the google spreadsheet, and a short identifier which will be used as the filename of the converted file.

The template includes a hidden row which contains markup that we can use to convert from the spreadsheet to RDF. This uses the taglifter.py module which was written for this project, as an experiment in finding terse ways to mark-up spreadsheets for conversion to RDF. 

The output will drop into the /data/ directory, ready to be loaded into a named graph on ResourceProjects.org
