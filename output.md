# output from running the deploy command

## sample output

```bash
:> ./deploy.sh
As of Cloud SDK 492.0.0 release, new functions will be deployed as 2nd gen functions by default. This is equivalent to currently deploying new with the --gen2 flag. Existing 1st gen functions will not be impacted and will continue to deploy as 1st gen functions.
You can disable this behavior by explicitly specifying the --no-gen2 flag or by setting the functions/gen2 config property to 'off'.
To learn more about the differences between 1st gen and 2nd gen functions, visit:
https://cloud.google.com/functions/docs/concepts/version-comparison
Preparing function...done.
✓ Deploying function...
  ✓ [Build] Logs are available at [https://console.cloud.google.com/cloud-build/builds;region=us
  -central1/3b8e13f4-448e-421a-8526-c623cf4aceb5?project=110539651778]
  ✓ [Service]
  . [ArtifactRegistry]
  . [Healthcheck]
  . [Triggercheck]
Done.
You can view your function in the Cloud Console here: https://console.cloud.google.com/functions/details/us-central1/run_report?project=emi-dev-env-2

buildConfig:
  automaticUpdatePolicy: {}
  build: projects/110539651778/locations/us-central1/builds/3b8e13f4-448e-421a-8526-c623cf4aceb5
  dockerRegistry: ARTIFACT_REGISTRY
  dockerRepository: projects/emi-dev-env-2/locations/us-central1/repositories/gcf-artifacts
  entryPoint: run_report
  runtime: python311
  serviceAccount: projects/emi-dev-env-2/serviceAccounts/110539651778-compute@developer.gserviceaccount.com
  source:
    storageSource:
      bucket: gcf-v2-sources-110539651778-us-central1
      generation: '1747632822602462'
      object: run_report/function-source.zip
  sourceProvenance:
    resolvedStorageSource:
      bucket: gcf-v2-sources-110539651778-us-central1
      generation: '1747632822602462'
      object: run_report/function-source.zip
createTime: '2025-05-19T05:33:42.846210522Z'
environment: GEN_2
labels:
  deployment-tool: cli-gcloud
name: projects/emi-dev-env-2/locations/us-central1/functions/run_report
satisfiesPzi: true
serviceConfig:
  allTrafficOnLatestRevision: true
  availableCpu: '0.1666'
  availableMemory: 256M
  environmentVariables:
    LOG_EXECUTION_ID: 'true'
  ingressSettings: ALLOW_ALL
  maxInstanceCount: 100
  maxInstanceRequestConcurrency: 1
  revision: run-report-00001-cal
  service: projects/emi-dev-env-2/locations/us-central1/services/run-report
  serviceAccountEmail: 110539651778-compute@developer.gserviceaccount.com
  timeoutSeconds: 60
  uri: https://run-report-bgnzyu4rja-uc.a.run.app
state: ACTIVE
updateTime: '2025-05-19T05:34:44.561662425Z'
url: https://us-central1-emi-dev-env-2.cloudfunctions.net/run_report


Updates are available for some Google Cloud CLI components.  To install them,
please run:
  $ gcloud components update



To take a quick anonymous survey, run:
  $ gcloud survey
```
