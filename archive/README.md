# Monster Archive

## BICCN
The original "Data Centers" team was meant to support scientific work in the BRAIN community.

### GitHub teams
* [Broad Pipeline Developers](https://github.com/orgs/BICCN/teams/broad-pipeline-developers) - Team for repositories under the `BICCN` org

### GitHub repos
* [CEMBA](https://github.com/biccn/cemba) - Analysis pipeline for single nucleus methylation data, handed off to Lantern
* [Terra Import Builder](https://github.com/BICCN/terra-import-builder) - Cloud function converting NeMO payloads into Terra import URLs,
                                                                          not actively maintained

## GDR
The original "Genomic Data Resources" team was meant to be a special-projects team
for proof-of-concept ingests.

### GitHub repos
* [GDR Ingest](https://github.com/broadinstitute/gdr-ingest) - Initial experiments at ingesting ENCODE data, archived

## Infrastructure
Monster has as strong culture of owning our own DevOps. We've gone through multiple
iterations of tracking configs while figuring out what works for us.

### GitHub repos
* [Monster Terraform](https://github.com/broadinstitute/terraform-monster) - Initial Terraform resources for a static Monster architecture, archived
* [Kafka Deploy](https://github.com/broadinstitute/emerald-kubernetes-kafka) - Initial experiments at managing Kafka and Zookeeper in Kubernetes, archived
* [Ingest Deploy](https://github.com/broadinstitute/dsp-ingest-deploy) - Terraform and Kubernetes configuration for deploying ingest components into GCP,
  based on the now-abandoned [dsp-k8s-deploy](https://github.com/broadinstitute/dsp-k8s-deploy)

## Ontology Service
We explored the possibility of running EBI's ontology service using our data model.

### GitHub repos
* [OLS Docker](https://github.com/broadinstitute/ols-docker) - Our fork of EBI's Ontology Lookup Service

## Data Ingest
Our first stabs at data ingest envisioned a framework of dataset-agnostic services.
We shifted away from that pattern because it introduced significant overhead vs. custom
pipelines using common command-line tools.

### GitHub repos
* [Ingester](https://github.com/broadinstitute/monster-ingester) - Service for orchestrating batch ingests into the Jade repo
* [Monster ETL](https://github.com/broadinstitute/monster-etl) - Apache Beam workflows for ingest
* [sbt plugins](https://github.com/broadinstitute/monster-sbt-plugins) - Common sbt plugins for our projects (merged with monster-scio-utils to become ingest-utils)
* [Scio utils](https://github.com/broadinstitute/monster-scio-utils) - Common Scio functionality for our pipelines (merged with monster-sbt-plugins to become ingest-utils)
