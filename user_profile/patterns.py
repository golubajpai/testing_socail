
from .views import *



getyourprofile=CreateProfile.as_view({'get':'list'})

createprofile=CreateProfile.as_view({'post':'create'})

update_profile= CreateProfile.as_view({'patch':'partial_update'})


get_interest_list= InterestList.as_view({'get':'list'})
create_interest_list= InterestList.as_view({'post':'create'})
update_interest_list=InterestList.as_view({'patch':'update'})
delete_interest_list= InterestList.as_view({'delete':'destroy'})


youfollowing_profile=Follow_Unfollow.as_view({'get':'list'})
follow=Follow_Unfollow.as_view({'post':'create'})
unfollow=Follow_Unfollow.as_view({'delete':'destroy'})