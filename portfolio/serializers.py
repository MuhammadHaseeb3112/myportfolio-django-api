from rest_framework import serializers

from .models import (
    PortfolioProfile,
    SocialLink,
    Skill,
    Hobby,
    Project,
    ProjectFeature,
    Testimonial,
    ContactMessage,
)


# ==========================================================
# Social Link Serializer
# ==========================================================

class SocialLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = SocialLink
        fields = "__all__"


# ==========================================================
# Skill Serializer
# ==========================================================

class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = "__all__"


# ==========================================================
# Hobby Serializer
# ==========================================================

class HobbySerializer(serializers.ModelSerializer):

    class Meta:
        model = Hobby
        fields = "__all__"


# ==========================================================
# Project Feature Serializer
# ==========================================================

class ProjectFeatureSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectFeature
        fields = (
            "id",
            "title",
        )


# ==========================================================
# Project Serializer
# ==========================================================
class ProjectSerializer(serializers.ModelSerializer):

    image_url = serializers.SerializerMethodField()

    features = ProjectFeatureSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Project
        fields = (
            "id",
            "company",
            "year",
            "title",
            "slug",
            "description",
            "image",
            "image_url",
            "github_url",
            "live_url",
            "featured",
            "display_order",
            "is_active",
            "features",
            "created_at",
            "updated_at",
        )

    def get_image_url(self, obj):
        request = self.context.get("request")
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None

# ==========================================================
# Testimonial Serializer
# ==========================================================

class TestimonialSerializer(serializers.ModelSerializer):

    avatar_url = serializers.SerializerMethodField()

    class Meta:
        model = Testimonial

        fields = (
            "id",
            "client_name",
            "position",
            "review",

            "avatar",
            "avatar_url",

            "display_order",

            "created_at",
            "updated_at",
        )

    def get_avatar_url(self, obj):
        request = self.context.get("request")

        if obj.avatar and request:
            return request.build_absolute_uri(obj.avatar.url)

        return None


# ==========================================================
# Contact Message Serializer
# ==========================================================

class ContactMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactMessage

        fields = (
            "id",
            "name",
            "email",
            "subject",
            "message",
            "created_at",
        )

        read_only_fields = (
            "created_at",
        )


# ==========================================================
# Portfolio Profile Serializer
# ==========================================================

class PortfolioProfileSerializer(serializers.ModelSerializer):

    profile_image_url = serializers.SerializerMethodField()

    resume_url = serializers.SerializerMethodField()

    social_links = SocialLinkSerializer(
        many=True,
        read_only=True
    )

    skills = SkillSerializer(
        many=True,
        read_only=True
    )

    hobbies = HobbySerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = PortfolioProfile

        fields = (
            "id",
            "full_name",
            "designation",
            "hero_title",
            "hero_description",
            "about",

            "profile_image",
            "profile_image_url",

            "resume",
            "resume_url",

            "email",
            "phone",
            "location",
            "map_url",
            "available_for_work",

            "social_links",
            "skills",
            "hobbies",

            "created_at",
            "updated_at",
        )

    def get_profile_image_url(self, obj):
        request = self.context.get("request")

        if obj.profile_image and request:
            return request.build_absolute_uri(obj.profile_image.url)

        return None

    def get_resume_url(self, obj):
        request = self.context.get("request")

        if obj.resume and request:
            return request.build_absolute_uri(obj.resume.url)

        return None