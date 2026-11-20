# Release checklist

Use this checklist for a candidate revision. Record commands, host versions,
results and links in [validation.md](validation.md). Complete the local
checks before requesting a publication decision.

## Prepare the candidate

- Confirm that `Zate/goals` is the intended public repository and that the
  MIT license and private GitHub security advisory reporting route are reflected
  in the release. Verify that repository and package license terms match.
- Choose a version and update all versioned marketplace and plugin manifests.
  Review the package identity, paths, descriptions and URLs.
- Review the README's local and hosted installation, first-session, refresh
  and removal instructions against the host versions being released.
- Run the deterministic package validator, unit tests and installer dry-run
  from the [validation guide](validation.md). Run the pinned Agent Skills
  validator and both Claude manifest validations.
- Verify the local marketplace lifecycle in fresh Codex and Claude Code
  profiles, including inventory, file hashes, refresh, removal and reinstall.
  Confirm the normal profiles are unchanged.
- Review the shared [behavioral cases](../evals/README.md) and the recorded
  user waiver of host model evaluations. The waiver leaves activation,
  workflow behavior and cross-host recovery unverified.
- Review the requirements in the [PRD](../PRD.md) against recorded evidence.
  Rerun affected checks after changes to the package, workflow or instructions.

## Decide and publish

- Record the exact candidate revision, version, package hashes and evidence.
  A documentation-only evidence commit can point to the tested source when
  package and workflow inputs are unchanged.
- Identify remaining hosted checks and limitations. Obtain explicit approval
  for the destination, version and revision before publishing.
- Publish the approved revision using the confirmed release mechanism.
  Record the remote reference and compare its resolved revision with the
  approved candidate.

## Verify the release

- Confirm the hosted Ubuntu and Windows validation jobs pass for the published
  revision and record their links.
- In fresh isolated profiles, install from the hosted marketplace in each host.
  Compare the resolved revision, version, skill inventory and installed file
  hashes with the candidate. Invoke the skill from a separate consumer
  repository.
- Record dated results, exact commands, platform and host versions in
  [validation.md](validation.md). Document any affected platform or operation
  if a check remains incomplete.

## Respond to a bad release

Record the affected version, observed failure and scope. Preserve evidence,
then use the confirmed distribution channel to withdraw or replace the release
with the owner's authorization. Fix the candidate, rerun affected checks, obtain
approval for the revised revision and version, and repeat hosted verification.
