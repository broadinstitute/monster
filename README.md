# The Monster Team
[![Monster Slack](https://img.shields.io/badge/Slack%20Channel-%23monster-blue.svg?style=flat)](https://broadinstitute.slack.com/messages/CCAU5L6LV/)
[![Monster CI Slack](https://img.shields.io/badge/Slack%20Channel-%23monster--ci-blue.svg?style=flat)](https://broadinstitute.slack.com/messages/CFXEDUUP5/)

New to the team? [Start here](./getting-started/README.md).

## People

| Name | Role | GitHub |
| --- | --- | --- |
| Dan Moran | Tech Lead | @danxmoran |
| Emily Munro-Ludders | Scrum Master | @emunrolu |
| Jeff Korte | Product Owner | @JeffKorte |
| Kathy Reinold | Data Modeler | @kreinold |
| Raaid Arshad | Software Engineer | @raaidbroad |
| Quazi Hoque | Software Engineer | @quazi-broad |
| Sarah Wessel | Software Engineer Co-op | @snwessel |

## GitHub Teams
* [DSP Monsters](https://github.com/orgs/broadinstitute/teams/dsp-monsters) - Team for repositories under the `broadinstitute` org
* [Emerald Writers](https://github.com/orgs/DataBiosphere/teams/broademeraldwrite) - Team for repositories under the `DataBiosphere` org

## Projects

### Data Modeling
Linked Data definitions for the DSP Core Data Model, with extensions for unmodeled datasets.

#### Documentation
* [Google Docs](https://drive.google.com/drive/folders/1n8TP4Q_4n2pCysjQz2Hkn2kpHGEILLCj)
* [Confluence - DSP Core Data Model](https://broadinstitute.atlassian.net/wiki/spaces/DSPCDM/overview)
* [Confluence - FAIR Community of Practice](https://broadinstitute.atlassian.net/wiki/spaces/FairCoP/overview)

#### GitHub repos
* [DSP Data Models](https://github.com/broadinstitute/dsp-data-models) - Data Model definitions and examples

### Data Ingest
Pipelines for moving data into the [Jade Data Repository](https://github.com/databiosphere/jade-data-repo).

#### Documentation
* [Google Docs](https://drive.google.com/drive/folders/1LjtBbMZs5-FqTGcRjw80ZBlHhfd_LT2z)

#### GitHub repos
* [ClinVar](https://github.com/DataBiosphere/clinvar-ingest) - ETL pipeline for the ClinVar dataset
* [ENCODE](https://github.com/DataBiosphere/encode-ingest) - ETL pipeline for the ENCODE dataset
* [Dog Aging](https://github.com/DataBiosphere/dog-aging-ingest) - ETL pipeline for the Dog Aging Project dataset

### Operations
Infrastructure, configuration, and shared code used to manage developing and deploying our services.

### GitHub repos
* [sbt plugins](https://github.com/broadinstitute/monster-sbt-plugins) - Common build plugins used across Monster projects
* [Helm charts](https://github.com/broadinstitute/monster-helm) - Custom Helm charts for pieces of Monster infrastructure
* [Core deployments](https://github.com/broadinstitute/monster-deploy) - Terraform modules, Helm releases, and deploy scripts
  for Monster's GCP environments

## Semi-Archived
The repositories in this section are still being used, but we're trying to move away from them.

### Data Ingest Framework
Our first stabs at data ingest envisioned a framework of dataset-agnostic services.
We shifted away from that pattern because it introduced significant overhead vs. custom
pipelines using common command-line tools.

#### GitHub repos
* [Transporter](https://github.com/databiosphere/transporter) - Bulk file-transfer system
* [Monster ETL](https://github.com/broadinstitute/monster-etl) - Apache Beam workflows for ingest
* [Extractors](https://github.com/broadinstitute/monster-extractors) - Tools / services for mechanically transforming external metadata into Beam-friendly JSON
* [Ingest Deploy](https://github.com/broadinstitute/dsp-ingest-deploy) - Terraform and Kubernetes configuration for deploying ingest components into GCP,
  based on the now-abandoned [dsp-k8s-deploy](https://github.com/broadinstitute/dsp-k8s-deploy)
* [Storage Libs](https://github.com/broadinstitute/monster-storage-libs) - Utility libraries for I/O against external storage systems
