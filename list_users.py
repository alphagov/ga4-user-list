from google.analytics.admin import AnalyticsAdminServiceClient
from google.analytics import admin_v1alpha
import pandas as pd
import functions_framework

project = 'ga4-analytics-352613'
analytics_client = AnalyticsAdminServiceClient()
# bq_client = bigquery.Client(project=project)
# parent = 'properties/294475112'


@functions_framework.http
def list_users():
    analytics_client = AnalyticsAdminServiceClient()
    request = admin_v1alpha.ListAccountsRequest()
    accounts = analytics_client.list_accounts(request=request)
    user_list = []
    for account in accounts:
        request = admin_v1alpha.ListPropertiesRequest(
            filter=f"parent:{account.name}",)
        properties = analytics_client.list_properties(request=request)
        for property in properties:
            users = analytics_client.list_access_bindings(parent=property.name)
            for user in users:
                email = user.user
                binding = user.name
                roles = user.roles
                data = {'email': email, 'binding': binding, 'roles': roles}
                user_list.append(data)
    df = pd.DataFrame(user_list, dtype='string')
    table_id = 'user_admin.all_users'
    df.to_gbq(table_id, project_id=project, if_exists='replace')
    print("done")


if __name__ == '__main__':
    list_users()
