from django.contrib import admin
from django.utils.html import format_html

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
# Project Feature Inline
# ==========================================================

class ProjectFeatureInline(admin.TabularInline):
    model = ProjectFeature
    extra = 1
    min_num = 1


# ==========================================================
# Portfolio Profile
# ==========================================================

@admin.register(PortfolioProfile)
class PortfolioProfileAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "designation",
        "email",
        "available_for_work",
        "created_at",
    )

    search_fields = (
        "full_name",
        "designation",
        "email",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
        "profile_preview",
    )

    fieldsets = (
        ("Basic Information", {
            "fields": (
                "full_name",
                "designation",
                "hero_title",
                "hero_description",
                "about",
            )
        }),

        ("Media", {
            "fields": (
                "profile_image",
                "profile_preview",
                "resume",
            )
        }),

        ("Contact Information", {
            "fields": (
                "email",
                "phone",
                "location",
                "map_url",
            )
        }),

        ("Settings", {
            "fields": (
                "available_for_work",
            )
        }),

        ("System Information", {
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )

    def profile_preview(self, obj):
        if obj.profile_image:
            return format_html(
                '<img src="{}" width="80" style="border-radius:8px;" />',
                obj.profile_image.url,
            )
        return "No Image"

    profile_preview.short_description = "Profile Preview"


# ==========================================================
# Social Links
# ==========================================================

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):

    list_display = (
        "platform",
        "profile",
        "display_order",
    )

    list_filter = (
        "platform",
    )

    search_fields = (
        "platform",
        "url",
    )

    ordering = (
        "display_order",
    )


# ==========================================================
# Skills
# ==========================================================

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
        "profile",
        "display_order",
    )

    list_filter = (
        "category",
    )

    search_fields = (
        "name",
    )

    ordering = (
        "display_order",
    )


# ==========================================================
# Hobbies
# ==========================================================

@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "emoji",
        "display_order",
    )

    search_fields = (
        "title",
    )

    ordering = (
        "display_order",
    )


# ==========================================================
# Projects
# ==========================================================

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    inlines = [ProjectFeatureInline]

    list_display = (
        "title",
        "company",
        "year",
        "featured",
        "is_active",
        "image_preview",
    )

    list_filter = (
        "featured",
        "is_active",
        "year",
    )

    search_fields = (
        "title",
        "company",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    ordering = (
        "display_order",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
        "image_preview",
    )

    fieldsets = (
        ("Project Information", {
            "fields": (
                "company",
                "year",
                "title",
                "slug",
                "description",
            )
        }),

        ("Links", {
            "fields": (
                "github_url",
                "live_url",
            )
        }),

        ("Image", {
            "fields": (
                "image",
                "image_preview",
            )
        }),

        ("Settings", {
            "fields": (
                "featured",
                "is_active",
                "display_order",
            )
        }),

        ("System", {
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="120" style="border-radius:10px;" />',
                obj.image.url,
            )
        return "No Image"

    image_preview.short_description = "Preview"


# ==========================================================
# Testimonials
# ==========================================================

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):

    list_display = (
        "client_name",
        "position",
        "avatar_preview",
    )

    search_fields = (
        "client_name",
        "position",
    )

    readonly_fields = (
        "avatar_preview",
    )

    ordering = (
        "display_order",
    )

    def avatar_preview(self, obj):
        if obj.avatar:
            return format_html(
                '<img src="{}" width="80" style="border-radius:50%;" />',
                obj.avatar.url,
            )
        return "No Avatar"

    avatar_preview.short_description = "Avatar"


# ==========================================================
# Contact Messages
# ==========================================================

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "subject",
        "is_read",
        "created_at",
    )

    list_filter = (
        "is_read",
    )

    search_fields = (
        "name",
        "email",
        "subject",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = (
        "-created_at",
    )