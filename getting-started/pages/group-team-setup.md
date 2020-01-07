# Join Groups / Teams / Channels
Monster's work spans multiple web platforms and organizations. Follow the steps
below to be sure you get access to everything you need.

## Slack Channels

### Main Channels
Join these channels for sure:
* `#105b` (building / facilities)
* `#dsde-emeraldempire` (Data Engineering)
* `#dsp-engineering`
* `#monster` (Public to Broad, includes members from other teams & leadership)
* `#monster-internal` (Private to Monster, ask a teammate to add you)
* `#prometheus` (DSP-wide)

### Tech Topics
You might find these channels useful for tech discussions:
* `#kubernetes`
* `#scala`
* `#softeng`

### Other Emerald Teams
Join some or all of these to keep tabs on other groups in Data Eng:
* `#dsde-ops` (Private; Genomics Platform operations)
* `#dsp-jade` (Data repository)
* `#green-hornet` (Genomics Platform & HCA infrastructure)
* `#green-lantern` (Genomics Platform & HCA scientific pipelines)
* `#wintergreen` (Private; Epigenomics Program pipelines and infrastructure)

`#dsp-jade` is the most relevant for now.

## GitHub Teams
Our GitHub repositories are spread across a few organizations.

### broadinstitute
This is the default org that you joined on your first day. Ask the Tech Lead to add you to
these teams:
* [DSP Monsters](https://github.com/orgs/broadinstitute/teams/dsp-monsters)

### DataBiosphere
This org hosts repositories that we feel aren't necessarily tied to Broad infrastructure
or use-cases. Multiple other institutes / companies are included in the org, so only a few
Broad members have the power to add other users.

Have the Tech Lead email the current Broad admins to get you added to the org, then made a
member of these teams:
* [Emerald Writers](https://github.com/orgs/DataBiosphere/teams/broademeraldwrite)

## DockerHub
We host containers for our open-source services in DockerHub. Go [here](https://hub.docker.com/)
to set up an account. Once it's set up, ask the Tech Lead to get you added to the `broadinstitute`
organization and DSDE team within.

## Quay
Our workloads can cause scalability issues in DockerHub by concurrently pulling a large
number of images. To avoid hitting this problem, we sometimes choose to host at-risk images
(usually containing command-line programs for scientific workflows) in [Quay](https://quay.io).
Set up an account, and ask the Tech Lead to get you added to the `broadinstitute` organization
and the Monster team within.

## Terra
[Terra](https://terra.bio/) is DSP's flagship product for biomedical research in the cloud.
Monster interacts with Terra's backend to set up ingested datasets. Set up dev and prod accounts
so you can interact with the systems directly when needed.

### Production
1. Visit the [production Terra app](https://app.terra.bio/)
2. Open the hamburger menu in the top-left, and click the Google sign-in option. Log in with
   your Broad identity.
3. Accept the Terms of Service.
4. Ask the Tech Lead to add you to these Terra groups as a member:
   * [Data Repository Stewards](https://app.terra.bio/#groups/Stewards)

### Dev
1. Create a throwaway gmail account. We don't use our main Google identities in dev
   in case credentials are accidentally exposed. For the sake of other dev users, we suggest
   using a name like `monster.<your-name>.dev@gmail.com`.
2. Visit the [dev Terra app](https://bvdp-saturn-dev.appspot.com/)
3. Open the hamburger menu in the top-left, and click the Google sign-in option. Log in with
   your new identity.
4. Accept the Terms of Service.
5. Ask a teammate to add you to these Terra groups as an admin:
   * [Data Repository Stewards](https://bvdp-saturn-dev.appspot.com/#groups/JadeStewards-dev)
   * [Data Repository Custodians](https://bvdp-saturn-dev.appspot.com/#groups/JadeCustodians-dev)

## AWS
We maintain a space in AWS for testing our file-transfer systems. The need is uncommon
enough across DSP that DevOps hasn't set up an automated process for acquiring an account,
so work with the Tech Lead to get into the system.

Once you have an account, follow these steps to set up local credentials:
1. Find yourself in the [list of users](https://console.aws.amazon.com/iam/home?region=us-east-1#/users),
   and click the link for your username.
2. Select the "Security Credentials" page.
3. Click "Create access key" to generate a new key ID / secret pair. Copy the secret
   key (or download the CSV).
4. Add your credentials to your local bash environment. To avoid accidentally sharing the secrets,
   we recommend you store them in their own file and then `source` them into your profile:
   ```bash
   # Write config to disk.
   mkdir -p ~/.config/aws
   /bin/cat <-EOF > ~/.config/aws/env
   export AWS_ACCESS_KEY_ID=<your-key-id>
   export AWS_SECRET_ACCESS_KEY=<your-secret>
   EOF

   # Load configs into your profile.
   echo "source '${HOME}/.config/aws'" >> ~/.bash_profile
   ```
