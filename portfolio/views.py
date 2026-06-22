from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import (
    PortfolioProfile,
    SocialLink,
    Skill,
    Hobby,
    Project,
    Testimonial,
    ContactMessage,
)

from .serializers import (
    PortfolioProfileSerializer,
    SocialLinkSerializer,
    SkillSerializer,
    HobbySerializer,
    ProjectSerializer,
    TestimonialSerializer,
    ContactMessageSerializer,
)


# ==========================================================
# Portfolio Profile API
# ==========================================================

class PortfolioProfileView(APIView):
    """
    Returns the portfolio owner's complete profile along with
    social links, skills and hobbies.
    """

    permission_classes = [AllowAny]

    def get(self, request):

        profile = (
            PortfolioProfile.objects
            .prefetch_related(
                "social_links",
                "skills",
                "hobbies",
            )
            .first()
        )

        if not profile:
            return Response(
                {"detail": "Portfolio profile not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = PortfolioProfileSerializer(
            profile,
            context={"request": request},
        )

        return Response(serializer.data)


# ==========================================================
# Social Links API
# ==========================================================

class SocialLinkViewSet(viewsets.ModelViewSet):
    """
    CRUD API for social media links.
    """

    serializer_class = SocialLinkSerializer
    permission_classes = [AllowAny]

    filter_backends = [OrderingFilter]

    ordering = ["display_order"]
    ordering_fields = ["display_order", "platform"]

    def get_queryset(self):
        return SocialLink.objects.all().order_by("display_order")


# ==========================================================
# Skills API
# ==========================================================

class SkillViewSet(viewsets.ModelViewSet):
    """
    CRUD API for portfolio skills.
    """

    serializer_class = SkillSerializer
    permission_classes = [AllowAny]

    filter_backends = [SearchFilter, OrderingFilter]

    search_fields = [
        "name",
        "category",
    ]

    ordering = ["display_order"]
    ordering_fields = [
        "display_order",
        "name",
        "category",
    ]

    def get_queryset(self):
        return (
            Skill.objects
            .select_related("profile")
            .order_by("display_order")
        )


# ==========================================================
# Hobbies API
# ==========================================================

class HobbyViewSet(viewsets.ModelViewSet):
    """
    CRUD API for hobbies.
    """

    serializer_class = HobbySerializer
    permission_classes = [AllowAny]

    filter_backends = [OrderingFilter]

    ordering = ["display_order"]
    ordering_fields = ["display_order", "title"]

    def get_queryset(self):
        return (
            Hobby.objects
            .select_related("profile")
            .order_by("display_order")
        )


# ==========================================================
# Projects API
# ==========================================================

class ProjectViewSet(viewsets.ModelViewSet):
    """
    CRUD API for portfolio projects.
    Returns project features and gallery images.
    """

    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]

    filter_backends = [SearchFilter, OrderingFilter]

    search_fields = [
        "title",
        "company",
        "description",
    ]

    ordering = ["display_order"]

    ordering_fields = [
        "display_order",
        "year",
        "title",
    ]

    def get_queryset(self):
        return (
            Project.objects
            .filter(is_active=True)
            .prefetch_related(
                "features",
                "gallery",
            )
            .order_by("display_order")
        )

# ==========================================================
# Testimonials API
# ==========================================================

class TestimonialViewSet(viewsets.ModelViewSet):
    """
    CRUD API for testimonials.
    """

    serializer_class = TestimonialSerializer
    permission_classes = [AllowAny]

    filter_backends = [OrderingFilter]

    ordering = ["display_order"]

    ordering_fields = [
        "display_order",
        "client_name",
    ]

    def get_queryset(self):
        return (
            Testimonial.objects
            .all()
            .order_by("display_order")
        )


# ==========================================================
# Contact Messages API
# ==========================================================

class ContactMessageViewSet(viewsets.ModelViewSet):
    """
    Contact form API.
    """

    serializer_class = ContactMessageSerializer
    permission_classes = [AllowAny]

    http_method_names = [
        "get",
        "post",
        "delete",
    ]

    filter_backends = [
        SearchFilter,
        OrderingFilter,
    ]

    search_fields = [
        "name",
        "email",
        "subject",
    ]

    ordering = [
        "-created_at",
    ]

    ordering_fields = [
        "created_at",
        "name",
        "email",
    ]

    def get_queryset(self):
        return ContactMessage.objects.all().order_by("-created_at")