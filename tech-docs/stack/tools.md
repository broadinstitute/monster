# Tools
Monster uses multiple tools within / in support of the ETL [systems](./systems.md)
that drive its ingest pipelines.

## Scio
Scio is a [Scala](./languages.md#scala) API for Apache Beam's Java SDK.

### Use case
All of the pipelines we run in [Dataflow](./systemd.md#dataflow) are written using Scio.

### Why Scio?
Beam's Java API is very verbose, and un-idiomatic for Scala code. Scio provides wrappers
and conversions that make the API more Scala-friendly. It also provides many helpers for
executing I/O against external storage systems, i.e. [BigQuery](./systems.md#bigquery).

Scio is maintained by Spotify, which uses the library + Dataflow for its data processing.

### Useful links
* [Scio site](https://spotify.github.io/scio/)

## sbt
sbt is an interactive build tool for [Scala](./languages.md#scala).

### Use case
Our [Scio](#scio) pipelines are built using sbt. We also use custom build logic to generate
`case class` definitions from schema definitions for the [Jade Repository](./systems.md#jade-repository),
helping us to keep both in sync.

### Why sbt?
sbt is the de facto "official" build tool for Scala. It comes pre-packaged with essential
tooling like incremental compilation and library resolution. It has a large plugin ecosystem
for adding features like git-based versioning and Dockerfile generation, and users can add
arbitrary build logic to existing steps using build-level Scala code. This extensibility makes
it straightforward to inject code generation logic and ensure that pipelines only compile if
the generated code compiles.

### Useful links
* [sbt documentation](https://www.scala-sbt.org/1.x/docs/)
* [Monster sbt-plugins repo](https://github.com/broadinstitute/monster-sbt-plugins)

## Terraform
Terraform is an infrastructure-as-code tool.

### Use case
We use Terraform to set up the pieces of our cloud infrastructure that run outside of
[Kubernetes](./systems.md#kubernetes), including the k8s clusters themselves.

### Why Terraform?
Terraform is DSP DevOps' tool/language of choice for managing cloud infrastructure.
Common configuration blocks can be abstracted into modules and imported from disk / git.
Cross-cloud environments can be managed from a single source of truth, with the details
of GCP vs. AWS APIs abstracted away.

### Useful links
* [Terraform getting started course](https://learn.hashicorp.com/terraform?track=gcp#gcp)
* [Terraform documentation](https://www.terraform.io/docs/cli-index.html)

## Helm
Helm is an infrastructure-as-code tool for Kubernetes.

### Use case
We use Helm to template-ize, package, and deploy the pieces of our cloud infrastructure
that run inside of [Kubernetes](./systems.md#kubernetes).

### Why Helm?
Helm is the de facto "official" solution for converting k8s manifests into reusable templates.
It is supported by the [CNCF](https://www.cncf.io/) and has a decent plugin ecosystem.

[Terraform](#terraform) also has support for deploying template-d manifests into Kubernetes,
but it has many known issues and forces using Terraform's [HCL](./languages.md#hcl) instead
of standard [YAML](./languages.md#yaml).

### Useful links
* [Helm documentation](https://helm.sh/docs/)
* [Intro to Helm slides](https://static.sched.com/hosted_files/kccncna19/7c/Helm%20Intro.pdf)

## Ad-Hoc tools
Some ingest pipelines have dataset-specific requirements that can't be met by our "standard"
suite of systems and tools.

### Use case
When a pipeline requires custom functionality, we'll use whatever tool gets the job done. If
we can't find an existing tool, we'll write one ourselves. For example:
* We use `wget` and `s3Cmd` to download files from FTP sites and S3 buckets
* We use `gsutil` to upload files to [GCS](./systems.md#google-cloud-storage) buckets
* We wrote a generic XML-to-JSON-list converter to process ClinVar archives

The tools are packaged into Docker containers and run as steps in an [Argo](./systems.md#argo)
workflow.

### Why Ad-Hoc tools?
Every source system we pull from has a slightly different API. It's unrealistic to expect
that we'll be able to force every pipeline into a uniform mold. Developing a strategy for
injecting the use of ad-hoc tooling into our ingest flows keeps us flexible, and allows us
to deliver greater value to each stakeholder.

### Useful links
* [`s3Cmd` repo](https://github.com/s3tools/s3cmd)
* [`gsutil` documentation](https://cloud.google.com/storage/docs/gsutil)
* [XML-to-JSON tool repo](https://github.com/broadinstitute/monster-extractors)
