# The Monster Team
[![Monster Slack](https://img.shields.io/badge/Slack%20Channel-%23monster-blue.svg?style=flat)](https://broadinstitute.slack.com/messages/CCAU5L6LV/)
[![Monster CI Slack](https://img.shields.io/badge/Slack%20Channel-%23monster--ci-blue.svg?style=flat)](https://broadinstitute.slack.com/messages/CFXEDUUP5/)

New to the team? [Start here](./getting-started/README.md).

## People

| Name | Role | GitHub |
| --- | --- | --- |
| Martina Goodlin | Scrum Master | NA |
| Jeff Korte | Product Owner | @JeffKorte |
| Kathy Reinold | Data Modeler | @kreinold |
| Raaid Arshad | Software Engineer | @raaidbroad |
| Quazi Hoque | Software Engineer | @quazi-broad |

## GitHub Teams
* [DSP Monsters](https://github.com/orgs/broadinstitute/teams/dsp-monsters) - Team for repositories under the `broadinstitute` org
* [Emerald Writers](https://github.com/orgs/DataBiosphere/teams/broademeraldwrite) - Team for repositories under the `DataBiosphere` org

## Projects

### Data Modeling
Linked Data definitions for the Terra Core Data Model, with extensions for unmodeled datasets.

#### Documentation
* [Google Docs](https://drive.google.com/drive/folders/1n8TP4Q_4n2pCysjQz2Hkn2kpHGEILLCj)
* [Confluence - DSP Core Data Model](https://broadinstitute.atlassian.net/wiki/spaces/DSPCDM/overview)
* [Confluence - FAIR Community of Practice](https://broadinstitute.atlassian.net/wiki/spaces/FairCoP/overview)

#### GitHub repos
* [TerraCore Data Model](https://github.com/DataBiosphere/terra-core-data-model) - Data Model definitions and examples

### Data Ingest
Pipelines for moving data into the [Jade Data Repository](https://github.com/databiosphere/jade-data-repo).

#### Documentation
* [Google Docs](https://drive.google.com/drive/folders/1LjtBbMZs5-FqTGcRjw80ZBlHhfd_LT2z)

#### GitHub repos
* [ClinVar](https://github.com/DataBiosphere/clinvar-ingest) - ETL pipeline for the ClinVar dataset
* [ENCODE](https://github.com/DataBiosphere/encode-ingest) - ETL pipeline for the ENCODE dataset
* [Dog Aging](https://github.com/DataBiosphere/dog-aging-ingest) - ETL pipeline for the Dog Aging Project dataset
* [HCA](https://github.com/DataBiosphere/hca-ingest) - ETL pipeline for the HCA

### Ingest Utilities
Tools and libraries used to support the top-level ingest pipelines.

#### GitHub repos
* [Base utilities](https://github.com/DataBiosphere/ingest-utils) - Common utilities shared across our batch ETL projects
* [XML-to-JSON-list](https://github.com/broadinstitute/monster-xml-to-json-list) - Command-line tool for mechanical
  conversion of XML into Beam-friendly JSON

### Operations
Infrastructure, configuration, and shared code used to manage developing and deploying our services.

### GitHub repos
* [Helm charts](https://github.com/broadinstitute/monster-helm) - Custom Helm charts for pieces of Monster infrastructure
* [Core deployments](https://github.com/broadinstitute/monster-deploy) - Terraform modules, Helm releases, and deploy scripts
  for Monster's GCP environments
* [setup-chart-releaser](https://github.com/broadinstitute/setup-chart-releaser) - GitHub Action to install [Chart Releaser](https://github.com/helm/chart-releaser)

## Semi-Archived
The repositories in this section are still being used, but we're trying to move away from them.

### Data Ingest Framework
Our first stabs at data ingest envisioned a framework of dataset-agnostic services.
We shifted away from that pattern because it introduced significant overhead vs. custom
pipelines using common command-line tools.

#### GitHub repos
* [Transporter](https://github.com/databiosphere/transporter) - Bulk file-transfer system
* [Storage Libs](https://github.com/broadinstitute/monster-storage-libs) - Utility libraries for I/O against external storage systems
