# Systems
Monster uses multiple ETL systems in its ingest workflows. Each system is
meant to cover a different type of processing / logic.

## Dataflow
Dataflow is a Google Cloud Service for running fully-managed data transformation
pipelines.

### Use case
We use Dataflow to handle row-level transformations of tabular data / metadata.
This includes:
* Renaming columns
* Converting column values to a different type / format
* Splitting rows into multiple tables
* Merging rows into a single table

### Why Dataflow?
Dataflow is fully managed and supports auto-scaling, so using it removes a significant
DevOps burden from the team. It has tight integration with other GCP services, but
also runs well in local mode. Finally, it includes a decent monitoring UI, so it's easy
for us to check the status of pipelines as they run.

### Related language(s)
Dataflow wraps Apache Beam's SDKs, so pipelines can be written in Python, Go, or
a JVM language. We use the JVM SDK because it's the most feature-complete, and
write our pipelines in [Scala](./languages.md#scala).

### Related tool(s)
We use the [Scio](./tools.md#scio) library to write pipelines against Beam's Java SDK.

### Useful links
* [Dataflow documentation](https://cloud.google.com/dataflow/docs/)
* [Beam documentation](https://beam.apache.org/documentation/)

## Argo
Argo is a workflow engine for running complex sequences of jobs on [Kubernetes](#kubernetes).

### Use case
We use Argo both as the main scheduler for our ingest pipelines and as
the executor for "weird" processing that doesn't fit nicely into Dataflow's
structured format. For example:
* Running a series of command-line tools written in different languages
* Interacting with data outside of Google Cloud
* Processing data at the file level, instead of the row level

### Why Argo?
Argo is a relatively young project, but it has been adopted by many large companies.
Intuit purchased the start-up that founded the project, and continues to develop it.
Google's Kubeflow project uses Argo as a back-end. Like Dataflow, it includes a UI for
monitoring workflows.

### Related language(s)
Argo workflows are specified as custom [Kubernetes](#kubernetes) objects in
[YAML](./languages.md#yaml) manifests. This is good because it prevents us from needing
to learn yet another workflow DSL. This is bad because YAML can be a pain to write.

[Bash](./languages.md#bash) and [Python](./languages.md#python) are also straightforward
to use within the "leaf" steps of Argo workflows. Scripts can be specified as multi-line
YAML strings inside of workflow specs.

### Related tool(s)
Each "leaf" step in an Argo workflow invokes a command-line tool within some Docker container.
These [tools](./tools.md#ad-hoc-tools) can be written in any language, and packaged in any
container that's accessible to the Kubernetes cluster running the workflow.

### Useful links
* [Initial investigation notes](https://docs.google.com/document/d/1EcLj-tJ5uQG0Ny7CwJ8NQiiKmEmCLIQcVm6b6b3bgWk/edit?usp=sharing)
* [Main Argo site](https://argoproj.github.io/argo)
* [Detailed workflow examples](https://argoproj.github.io/docs/argo/examples/readme.html)
* [Kubernetes CRD documentation](https://kubernetes.io/docs/tasks/access-kubernetes-api/custom-resources/custom-resource-definitions/)
* [Python client for Argo](https://github.com/CermakM/argo-client-python)

## Jade Repository
The Jade Repository is the main product of our sibling team, and the "sink" for all of
the data we ingest.

### Use case
Apart from making the data we process available to others, we use the Jade repository to
handle ETL steps that would be difficult to execute from outside the system. For example:
* Update-or-insert for tabular data
* GUID assignment for files
* Cross-linking tabular data to files

### Why Jade?
We expect that Monster will own / maintain relatively little of the data stored in the Jade
Repository. Contributing truly generic functionality to the repo's codebase allows us to
enforce some level of uniformity in the datasets that we have no control over. It also reduces
the barrier to entry for other groups that would like to publish into the repository, improving
the entire ecosystem.

### Related language(s)
The Repository's back-end is written in [Java](./languages.md#java).

### Useful links
* [Jade GitHub repo](https://github.com/databiosphere/jade-data-repo)
* [Jade tech docs](https://drive.google.com/drive/u/0/folders/1njMO20WaretNaZ7NxnKGyu20N9VmhB6K)

## BigQuery
BigQuery is a Google Cloud service providing a serverless, SQL-esque data warehouse.

### Use case
BigQuery (BQ) is the storage system backing tabular data in the [Jade Repository](#jade-repository).
The schemas we design for our datasets are optimized for BQ's quirks. We also expect that our
[Dataflow](#dataflow) pipelines may eventually need to read from existing BQ datasets to run
de-duplication logic.

### Why BigQuery?
The Jade team has the most detail, but at a high level:
* BQ is optimized for append-only workflows, which fits nicely into the ideal of scientific
  reproducibility (no updating rows in-place)
* BQ is "infinitely scalable", so we don't need to worry about datasets becoming too large
* BQ queries can span datasets stored in different projects / locations
* BQ separates billing for storage & access of data, reducing the burden of egress charges
  on data generators
* BQ supports cell-level access control, making it easy to share data without copying it

### Related language(s)
Data is access in BigQuery using a dialect of [SQL](./languages.md#sql).

### Useful links
* [BigQuery documentation](https://cloud.google.com/bigquery/docs/)
* [One-page function reference](https://cloud.google.com/bigquery/docs/reference/standard-sql/functions-and-operators)

## Google Cloud Storage
Cloud Storage is a Google Cloud service providing serverless object storage.

### Use case
Cloud Storage (GCS) is the storage system backing file data in the [Jade Repository](#jade-repository).
It's also the system we use for intermediate storage when passing data between systems in our
ingest pipelines.

### Why GCS?
GCS is the cheapest, most scalable way to store arbitrary data in Google Cloud. Both
[Dataflow](#dataflow) and [BigQuery](#bigquery) can efficiently read data directly from
GCS buckets. Object-level access control makes sharing data easy.

### Useful links
* [Cloud Storage documentation](https://cloud.google.com/storage/docs/)

## Kubernetes
Kubernetes is a container orchestration / management system.

### Use case
Apart from [Dataflow](#dataflow), [BigQuery](#bigquery), and [Cloud Storage](#google-cloud-storage),
all of our applications are managed by Kubernetes (k8s). The system provides a uniform API for
specifying deployments, and automated mechanisms for detecting & restarting unhealthy systems.

### Why Kubernetes?
k8s is the de-facto standard for running complex containerized applications. It was originally built
by Google, but now has significant support from every major cloud vendor. Targeting its API (instead
of Google-specific APIs / scripts) prevents us from being fully locked into GCP.

### Related language(s)
k8s manifests are typically specified in [YAML](./languages.md#yaml).

### Related tool(s)
[Helm](./tools.md#helm) is a tool for packaging k8s manifests as reusable templates, and for combining
those templates into a concrete deployment.

### Useful links
* [Kubernetes documentation](https://kubernetes.io/docs/home/)
* [Intro to k8s edX course](https://www.edx.org/course/introduction-to-kubernetes)
* [Google Kubernetes Engine documentation](https://cloud.google.com/kubernetes-engine/docs/)

## Flux Helm Operator
The Flux Helm Operator is a GitOps engine for deploying Helm releases in [Kubernetes](#kubernetes).

### Use case
We use the Helm Operator to track Helm definitions in git, re-deploying whenever a branch is updated
or a tag is moved.

### Why the Helm Operator?
Traditional CI/CD pipelines add a "deploy" step to the end of (i.e.) a Jenkins pipeline. This is tough
to set up because you don't typically want to deploy every commit to every environment, so you end up
with a complex, brittle pipeline. Even when pipelines succeed, there's no automated tracking to ensure
the deployment stays healthy over time.

Separating CD from CI allows the CI pipeline to stay simple and git-oriented. Running the CD operator
inside of the cluster it's deploying into enables automated health-checking and redeployment in the case
of failures.

### Related tool(s)
[Helm](./tools.md#helm) is the deployment mechanism used under-the-hood by the operator.

### Useful links
* [Helm Operator documentation](https://docs.fluxcd.io/projects/helm-operator/en/latest/)
* [Kubernetes CRD documentation](https://kubernetes.io/docs/tasks/access-kubernetes-api/custom-resources/custom-resource-definitions/)
