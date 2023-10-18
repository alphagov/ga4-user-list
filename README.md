# GA4_user_list
This produces a list of all users with access to the same accounts/ GA4 properties as you and saves the data in BigQuery.

This is designed to be run as a Google Cloud Function as a service account, remeber to give the service access access to the accounts / properties you want monitored.

This only lists users that have been granted access directly, it does not list out inherited access, for example if access is granted via membership to a Marketing Platform Group.


## Requirements


*   [Google Cloud Platform (GCP) project](https://cloud.google.com/resource-manager/docs/creating-managing-projects) with [billing enabled](https://cloud.google.com/billing/docs/how-to/modify-project#enable-billing) - Create or use an existing project as needed.
    *   Note: This solution uses billable GCP resources.
*   [Google Analytics](https://analytics.google.com/analytics/web/)


### Environment variables needed
These can be set in a `.env` file
`GCP_PROJECT_ID` The project to host the Cloud Function and the BigQuery data
`GA4_ENTITY` in the format `properties/123456` or `accounts/123456`