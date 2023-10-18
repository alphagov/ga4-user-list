from google.analytics.admin import AnalyticsAdminServiceClient
from google.analytics import admin_v1alpha
import pandas as pd
import functions_framework
import re

project = 'ga4-analytics-352613'
analytics_client = AnalyticsAdminServiceClient()


@functions_framework.http
def list_users():
    analytics_client = AnalyticsAdminServiceClient()
    request = admin_v1alpha.ListAccountsRequest()
    accounts = analytics_client.list_accounts(request=request)
    user_list = []
    for account in accounts:
        users = analytics_client.list_access_bindings(parent=account.name)
        for user in users:
            email = user.user
            binding = user.name
            roles = user.roles
            property_id = re.search(r'accounts\/\d*', binding)
            data = {'email': email, 'binding': binding, 'roles': roles, 'parent': property_id.group()}
            user_list.append(data)
        request = admin_v1alpha.ListPropertiesRequest(
            filter=f"parent:{account.name}",)
        properties = analytics_client.list_properties(request=request)
        for property in properties:
            users = analytics_client.list_access_bindings(parent=property.name)
            for user in users:
                email = user.user
                binding = user.name
                roles = user.roles
                property_id = re.search(r'properties\/\d*', binding)
                data = {'email': email, 'binding': binding, 'roles': roles, 'parent': property_id.group()}
                user_list.append(data)
    df = pd.DataFrame(user_list, dtype='string')
    table_id = 'user_admin.all_users'
    df.to_gbq(table_id, project_id=project, if_exists='replace')
    print("done")


@functions_framework.http
def run(request=None):
    try:
        list_users()
        return "all good"
    except Exception as e:
        print(e)
        return "all bad"


if __name__ == '__main__':
    run()
