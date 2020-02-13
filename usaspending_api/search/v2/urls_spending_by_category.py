from django.conf.urls import url

from usaspending_api.search.v2.views.spending_by_category_views.spending_by_agency_types import (
    AwardingAgencyViewSet,
    AwardingSubagencyViewSet,
    FundingAgencyViewSet,
    FundingSubagencyViewSet,
)

from usaspending_api.search.v2.views.spending_by_category_views.spending_by_location_types import CountryViewSet

urlpatterns = [
    url(r"^awarding_agency", AwardingAgencyViewSet.as_view()),
    url(r"^awarding_subagency", AwardingSubagencyViewSet.as_view()),
    url(r"^funding_agency", FundingAgencyViewSet.as_view()),
    url(r"^funding_subagency", FundingSubagencyViewSet.as_view()),
    url(r"^country", CountryViewSet.as_view()),
]
