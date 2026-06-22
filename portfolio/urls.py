from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    PortfolioProfileView,
    SocialLinkViewSet,
    SkillViewSet,
    HobbyViewSet,
    ProjectViewSet,
    TestimonialViewSet,
    ContactMessageViewSet,
)

# ==========================================================
# DRF Router
# ==========================================================

router = DefaultRouter()

router.register(
    r"social-links",
    SocialLinkViewSet,
    basename="social-links"
)

router.register(
    r"skills",
    SkillViewSet,
    basename="skills"
)

router.register(
    r"hobbies",
    HobbyViewSet,
    basename="hobbies"
)

router.register(
    r"projects",
    ProjectViewSet,
    basename="projects"
)

router.register(
    r"testimonials",
    TestimonialViewSet,
    basename="testimonials"
)

router.register(
    r"contact",
    ContactMessageViewSet,
    basename="contact"
)

# ==========================================================
# URL Patterns
# ==========================================================

urlpatterns = [

    # Portfolio Profile (Single Object)
    path(
        "profile/",
        PortfolioProfileView.as_view(),
        name="portfolio-profile",
    ),

    # Router URLs
    path(
        "",
        include(router.urls),
    ),
]