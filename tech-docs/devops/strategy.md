# Monster DevOps - Current Strategy
Where "current" translates to "beginning of Q1, 2020". If you've landed here
and see reality has drifted away from what's described, please update the docs!

## Environments
Monster maintains two environments: dev and prod. Infrastructure-as-code definitions for
both environments are tracked in the same [GitHub repository](https://github.com/broadinstitute/dsp-monster-core-infrastructure/).
Each environment spans multiple Google projects and GKE clusters.

### Dev vs. prod
Our dev environment is meant to serve as an internal integration space, where we test
if/how upgrading core services causes massive issues. It is also the space where we run
minimal "bleeding edge" versions of our ingest pipelines to flush out any problems.

Our production environment is where we run validated versions of our core services, and
pipelines that ingest data into the production Jade Repository.

Both dev and prod share a core set of configuration templates to ensure that they don't
drift too far apart. Dev is extended to include extra infrastructure and services required
for integration-testing.

#### No staging?
Other teams in DSP maintain a staging environment as a midpoint between dev and prod.
This sort of space is typically used to:
* Set up a production instance of a service that's cut off from the outside world, for
  cross-team integration testing
* Run a final suite of pre-release tests in a "clean room" environment, if dev is very
  unstable

We don't see the need for a staging environment in Monster because:
* We don't build services for use by other DSP teams, so there's no need for a cross-
  team integration space
* We believe we can effectively isolate our test spaces using separate Terraform modules
  and Kubernetes namespaces

If either of these points change, it could be worth introducing a third environment.

### Environment core
Monster's dev and prod environments share a "core" template outlining the infrastructure
needed to run ingest pipelines.

#### Prerequisite: Google projects and state buckets
The core template does not include Google project generation, since that action requires
write permissions on every associated billing project. Before we can set up the concrete
definition for an environment using our core template, we (monster@broadinstitute.org) must
have project-level Edit access on:
* A "command center" project associated with our team's billing account
* A "processing" project per distinct stakeholder billing account that should be charged
  for running ingest operations

For example, in dev we have:
* `broad-dsp-monster-dev` as the command center
* `broad-gdr-encode-dev` and `broad-dsp-monster-clingen-dev` as stakeholder-specific projects

Finally, in order to store Terraform state in Cloud Storage we need to manually create a bucket
(Terraform can't bootstrap its own backend by creating the bucket itself). We typically create the
bucket inside the command center project. For example, in dev we have `broad-dsp-monster-dev-terraform-state`.

#### Terraform
The GCP infrastructure in each Monster environment is configured using a single Terraform module.
Using a single module per environment helps us link resources across Google projects without
needing to share Terraform state-files across modules. The core of this module sets up different
resources for the "command center" and each "processing" project.

Within the command center, the module initializes:
1. GCP APIs required to run core apps/services
2. A Compute Engine network configured to access the public internet
3. A GKE cluster with a single static node pool, attached to the network
4. A DNS zone for apps/services running within the environment
5. Individual DNS entries within the zone for each app/service that needs one
6. Any databases needed to support apps/services running within the command center
7. Any IAM service accounts needed for authenticating with GCP / other Google systems
8. IAM bindings between the generated accounts and GCP resources

Within each processing project, the module initializes:
1. GCP APIs required to run processing apps/services (i.e. Dataflow)
2. A Compute Engine network configured to access the public internet
3. A GKE cluster with one static node pool, and
   [node auto-provisioning](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning)
   enabled
   * The static node pool is only large enough to run GKE's pre-loaded system pods
   * Auto-provisioning is configured to set taints on provisioned nodes, preventing
     system pods from migrating onto the generated machines
4. GCS buckets for storing project-specific artifacts and data
5. Any IAM service accounts needed for authenticating with GCP / other Google systems
6. IAM bindings between the generated accounts and GCP resources

The module also generates kubeconfig files for every created GKE cluster, and writes
them to local disk for use by downstream tools. Finally, it writes any sensitive configs
(i.e. database passwords) to Vault.

#### Namespaces
We initialize namespaces in GKE after baseline infrastructure is in place.

Within the command center cluster, we create namespaces for:
* The Flux CD `helm-operator`
* Airflow
* The Argo UI
* Each processing project (to host Argo controllers)

We create a single `argo` namespace in each processing cluster.

#### Helm releases
Finally, after carving out namespaces we use Helm to set up services in GKE. We install
a single Helm chart into every GKE cluster.

The command center's chart installs into the Flux CD namespace, creating:
1. The Flux CD `helm-operator` deployment
2. A `HelmRelease` CRD for Airflow, targeting its namespace
3. A `HelmRelease` CRD for the Argo UI, targeting its namespace
4. A `HelmRelease` CRD per processing project, targeting their respective namespaces to install:
   * An Argo workflow controller
   * Any project-specific GKE resources
5. Any pod security policies and RBAC rules required to get all the components above running

The specific versions tracked by each `HelmRelease` CRD are template-ized as values in the top-
level Helm chart, allowing us to use the same chart for environments of varying stability.

Each processing cluster's chart installs into the `argo` namespace, creating:
1. A service account to run Argo workflow pods
2. Any pod security policies and RBAC rules required to let the account run pods
3. Any pod security policies and RBAC rules required to let the corresponding Argo controller in
   the command center create and monitor pods

### Dev extensions
Monster's dev environment includes additional infrastructure and services on top of the
core template. These extra resources are maintained to support running end-to-end pipeline tests
in a controlled environment.

#### Terraform
Infrastructure-level dev extensions are included in the same top-level Terraform module as
core resources. The extensions generate things needed for testing, for example:
* AWS S3 buckets, and IAM users that can access those buckets
* GCP resources needed to run a test instance of the Jade Repository

#### Namespaces
On top of the core namespaces, the dev command center creates spaces for:
* The "Monster Test Repo"
* A test FTP server
* A test SFTP server

#### Helm releases
The top-level Helm chart for the dev command center includes additional `HelmRelease`
definitions for:
* An instance of the Jade Repository
* A test FTP server
* A test SFTP server
