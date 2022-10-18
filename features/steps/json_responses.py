import trafaret as t

"""
Example of using Trafaret (https://github.com/Deepwalker/trafaret) to describe json response structure
Assuming our json is:
{
   "access_token":"access_token",
   "refresh_token":"refresh_token",
   "token_type":"token_type",
   "expires_in":1800
}
Our trafaret will be:
tokenData = t.Dict({
    t.Key('access_token'): t.String,
    t.Key('refresh_token'): t.String,
    t.Key('token_type'): t.String,
    t.Key('expires_in'): t.Int
})
"""

# Below are objects used for validating response in test.feature
employeeData = t.Dict({
    t.Key('id'): t.Int,
    t.Key('employee_name'): t.String,
    t.Key('employee_salary'): t.Int,
    t.Key('employee_age'): t.Int,
    t.Key('profile_image'): t.String(allow_blank=True)

})

responseData = t.Dict({
    t.Key('status'): t.String,
    t.Key('data'): employeeData,
    t.Key('message'): t.String
})


