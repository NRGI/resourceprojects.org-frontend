% Data Model

To be able to rapidly iterate on the data model for ResourceProjects.org we have built on a [linked data](http://linkeddata.org/) model. Our data is therefore an extensible [graph structure](https://en.wikipedia.org/wiki/Graph_(abstract_data_type)), with a set of core entities and properties defined by an ontology.

The draft ontology [can be found here](https://github.com/NRGI/resource-projects-etl/blob/master/ontology/resource-projects-ontology.rdf) (RDF). 

A couple of initial notes that might help you exploring the data.

## Namespaces & mapping

Core properties are all in the [http://resourceprojects.org/def/](http://resourceprojects.org/def/) namespace. We use the prefix rp for this.

If we encounter properties in incoming files that are not declared in our ontology we mint URIs for these under [http://resourceprojects.org/def/misc/](http://resourceprojects.org/def/misc/) in order to keep track of them, and consider them for inclusion in the full ontology later. We use the prefix rp_misc for this. 

We have tried to use pattern from existing ontologies where possible.

### Stakeholding & memberships

One of the common modelling issues we need to deal with in resource projects data is the association between a company and a project, or between companies and groups.

Because these are subject to change over time, we model the relationship with an intermediate entity, either a rp:Stake, or rp:Membership.

Properties subject to change over time, such as percentage share, or status as operator of a project, attach to the Stake, rather than the company or project directly. 

#### Stakeholding relationships

The relationship between a project and company via Stake looks as follows:

![Project, Companies and Stakes model](/img/model-stakes.png)
