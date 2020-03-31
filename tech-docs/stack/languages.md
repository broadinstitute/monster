# Languages
Monster is a polyglot team. We typically pick languages based on the
requirements / available features of our chosen [ETL systems](./systems.md)
and [tools](./tools.md).

## Scala
Scala is a compiled, statically-typed language which runs on the JVM.

### Why Scala?
The original choice to use Scala was based on the personal preference of Monster's
first tech lead. Scala was also DSP's main language in its early years, so it was
easy to get code reviews from other teams. For this reason, our "legacy" projects are
predominantly written in Scala.

Compared to [Java](#java), Scala has better support for functional programming and a
more expressive type system, at the expense of longer compile times and a steeper learning
curve.

Our Scala usage has decreased since we decided to shift from building services
towards building dataset-specific pipelines. We still use it in places where:
* JVM languages have better support / more features than the alternatives, and/or
* Program logic is complex enough to benefit from strong, static typing

### Where do we use Scala?
1. [Dataflow](.systems.md#dataflow) pipelines, via the [Scio](./tools.md#scio) library.
2. Custom [sbt](./tools.md#sbt) build tasks, usually in support of the Dataflow pipelines.
3. Some [Ad-hoc tools](./tools.md#ad-hoc-tools).

### Useful links
* [Language homepage](https://scala-lang.org/)
* [Intro EdX course](https://courseware.epfl.ch/courses/course-v1:EPFL+progfun1+2018_T1/about)
* [Essential Scala](https://books.underscore.io/essential-scala/essential-scala.html)
* [Scala with Cats](https://books.underscore.io/scala-with-cats/scala-with-cats.html)
* (Satire) [Evolution of a Scala Programmer](https://medium.com/@olxc/the-evolution-of-a-scala-programmer-1b7a709fb71f)

## Java
Java is a compiled, statically-typed language which runs on the JVM.

### Why Java?
As part of the effort to rearchitect Terra, DSP and Verily agreed on Java
as the common language for all "core" services in the platform. We therefore
use Java whenever we contribute to those services.

DSP's Methods group also has deep knowledge and experience in Java from building
Picard & GATK, so it's easy to get good code reviews from other teams.

### Where do we use Java?
1. Contributions to the [Jade Repository](./systems.md#jade-repository)'s backend.

### Useful links
* [Java 8 API docs](https://docs.oracle.com/javase/8/docs/api/)
* ["Official" Java tutorials](https://docs.oracle.com/javase/tutorial/)
* [Google Java style guide](https://google.github.io/styleguide/javaguide.html)

## Python
Python is an interpreted, dynamically-typed language.

### Why Python?
Python's standard library is packed with helpful utilities, so it's a good choice for
scripts that do something other than just call out to other command-line tools.

Python is also a popular choice in the data science / data engineering field,
so we often end up using Python in order to use an existing ETL system or tool.

### Where do we use Python?
1. Ad-hoc scripts embedded within [Argo](./systems.md#argo) workflows.

### Useful links
* [Official Python tutorial](https://docs.python.org/3/tutorial/index.html)
* [Python style guide](https://www.python.org/dev/peps/pep-0008/)
* [Google's Python intro](https://developers.google.com/edu/python/introduction)

## Bash
Bash is a Unix shell and command language.

### Why Bash?
Bash is OK "glue" between other programs (especially command-line tools), and it
Just Works on most machines. It's a good choice for scripts that aren't complex
enough to justify worrying about version skew / dependency management of Python.

### Where do we use Bash?
1. Ad-hoc scripts embedded within [Argo](./systems.md#argo) workflows.
2. Deployment scripts that call [Terraform](./tools.md#terraform) and [Helm](./tools.md#helm).

### Useful links
* [Bash reference manual](https://www.gnu.org/software/bash/manual/bash.html)
* [SoftEng presentation on Shell](https://github.com/broadinstitute/tbl/blob/master/bash/notes.org)

## YAML
YAML is a data serialization format.

### Why YAML?
YAML isn't _really_ a programming language at its core. It's a common choice for
configuration files. A few systems also use it as a declarative pseudo-language
for describing steps in a workflow.

### Where do we use YAML?
1. [Kubernetes](./systems.md#kubernetes) manifests, rendered and deployed via [Helm](./tools.md#helm).
2. [Argo](./systems.md#argo) workflow definitions.

### Useful links
* [Official YAML site](https://yaml.org/)
* [YAML tutorial](https://rollout.io/blog/yaml-tutorial-everything-you-need-get-started/)

## HCL
HCL is a structured configuration language.

### Why HCL?
HCL was created by [Hashicorp](https://www.hashicorp.com/) to serve as a human-friendly
alternative to JSON and YAML. We use it when working with their products.

### Where do we use HCL?
1. [Terraform](./tools.md#terraform) module definitions.

### Useful links
* [HCL syntax spec](https://github.com/hashicorp/hcl/blob/hcl2/hclsyntax/spec.md)

## RDF-OWL
RDF-OWL is a serialization format for linked data.

### Why RDF-OWL?
The DSP Core Data Model (and nearly all external data models) are specified as "linked data" (RDF).
Of all the RDF serialization formats, we found that OWL was the easiest to review.

### Where do we use RDF-OWL?
We don't currently write OWL directly or access it in an automated way. The visual modeling tools
used by our data modeler export their definitions of OWL. We check these files in, and review them
in GitHub.

Our eventual hope is to find/build an "ontology service" which can consume RDF directly and provide
an API for humans and machines to inspect the model as part of Terra.

### Useful links
* [W3C OWL notes](https://www.w3.org/OWL/)
* [DSP Core Data Model repo](https://github.com/broadinstitute/dsp-data-models)

## SQL
SQL is a standard language for working with data stored in a database.

### Why SQL?
Every relational database on earth (and some non-relational ones) exposes a SQL interface. SQL is
also familiar to many technical "non-engineers" (i.e. the operations team, and bioinformaticians).

### Where do we use SQL?
ETL code we contribute to the [Jade Repository](./systems.md#jade-repository) often deals with SQL,
to manipulate data stored in [BigQuery](./systems.md#bigquery). [Dataflow](./systems.md#dataflow)
pipelines that access BigQuery data typically include a raw SQL query describing the data to pull.

### Useful links
* [PostgreSQL language reference](https://www.postgresql.org/docs/9.6/sql.html)
